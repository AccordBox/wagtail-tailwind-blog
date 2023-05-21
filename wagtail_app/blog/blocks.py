from wagtail.core.blocks import (BooleanBlock, CharBlock, ChoiceBlock,
                                 DateTimeBlock, FieldBlock, IntegerBlock,
                                 ListBlock, PageChooserBlock, RawHTMLBlock,
                                 RichTextBlock, StreamBlock, StructBlock,
                                 StructValue, TextBlock, URLBlock)
from wagtail.images.blocks import ImageChooserBlock
from wagtailmarkdown.blocks import MarkdownBlock


class ImageText(StructBlock):
    reverse = BooleanBlock(required=False)
    title = RichTextBlock(required=False)
    text = RichTextBlock()
    image = ImageChooserBlock()


class Testimonial(StructBlock):
    text = RichTextBlock(required=False)
    name = RichTextBlock(required=False)


class BodyBlock(StreamBlock):
    h1 = CharBlock()
    h2 = CharBlock()
    paragraph = RichTextBlock()
    markdown = MarkdownBlock(icon="code")



    testimonials = ListBlock(Testimonial())
    image_text = ImageText()
    image_carousel = ListBlock(ImageChooserBlock())
    thumbnail_gallery = ListBlock(ImageChooserBlock())
