-- Pandoc filter: render the Obsidian-flavoured lecture notes.
--   [[target]] / [[target|text]]  -> plain text
--   > [!type]- Title              -> Quarto callout (trailing - or + sets collapse)
local utils = require 'pandoc.utils'

local callout_type = { note = "note", info = "note", example = "note", quote = "note",
  question = "tip", success = "tip", tip = "tip", warning = "warning", important = "important",
  danger = "caution", caution = "caution" }

function Inlines(inlines)
  local out, i = pandoc.List(), 1
  while i <= #inlines do
    local el = inlines[i]
    if el.t == "Str" and el.text:find("%[%[") then
      local j, found = i, false
      while j <= #inlines and j - i < 12 do
        if inlines[j].t == "Str" and inlines[j].text:find("%]%]") then found = true break end
        j = j + 1
      end
      if found then
        local seg = pandoc.List()
        for k = i, j do seg:insert(inlines[k]) end
        local s = utils.stringify(pandoc.Plain(seg))
        local pre, inner, rest = s:match("^(.-)%[%[(.-)%]%](.*)$")
        local shown = inner:match("|(.*)$") or inner:gsub("-", " ")
        out:insert(pandoc.Str(pre .. shown .. rest))
        i = j + 1
      else
        out:insert(el); i = i + 1
      end
    else
      out:insert(el); i = i + 1
    end
  end
  return out
end

function BlockQuote(bq)
  local first = bq.content[1]
  if not first or (first.t ~= "Para" and first.t ~= "Plain") then return nil end
  local head = first.content[1]
  if not head or head.t ~= "Str" then return nil end
  local kind, flag = head.text:match("^%[!(%a+)%]([+-]?)$")
  if not kind then return nil end
  local title, body, in_title = pandoc.List(), pandoc.List(), true
  for k = 3, #first.content do
    local x = first.content[k]
    if in_title and (x.t == "SoftBreak" or x.t == "LineBreak") then in_title = false
    elseif in_title then title:insert(x) else body:insert(x) end
  end
  local blocks = pandoc.List()
  if #title > 0 then blocks:insert(pandoc.Header(2, title)) end
  if #body > 0 then blocks:insert(pandoc.Para(body)) end
  for k = 2, #bq.content do blocks:insert(bq.content[k]) end
  local attrs = {}
  if flag == "-" then attrs.collapse = "true" elseif flag == "+" then attrs.collapse = "false" end
  return pandoc.Div(blocks, pandoc.Attr("", { "callout-" .. (callout_type[kind:lower()] or "note") }, attrs))
end
