from django import template
from django.utils.html import format_html
from django.utils.safestring import mark_safe


register = template.Library()


@register.filter
def rich_text(value):
    blocks = [block.strip() for block in value.split('\n\n') if block.strip()]
    rendered_blocks = []

    for block in blocks:
        lines = [line.strip() for line in block.splitlines() if line.strip()]
        if not lines:
            continue
        text = ' '.join(lines)
        if text.startswith('### '):
            rendered_blocks.append(format_html('<h3>{}</h3>', text[4:]))
        elif text.startswith('## '):
            rendered_blocks.append(format_html('<h2>{}</h2>', text[3:]))
        else:
            rendered_blocks.append(format_html('<p>{}</p>', text))

    return mark_safe('\n'.join(rendered_blocks))
