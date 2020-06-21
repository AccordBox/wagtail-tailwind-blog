# Generated by Django 3.0.7 on 2020-06-20 16:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailmenus', '0023_remove_use_specific'),
        ('wagtailforms', '0004_add_verbose_name_plural'),
        ('wagtailredirects', '0006_redirect_increase_max_length'),
        ('wagtailcore', '0045_assign_unlock_grouppagepermission'),
        ('blog', '0004_remove_postpage_excerpt'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='formpage',
            name='page_ptr',
        ),
        migrations.DeleteModel(
            name='FormField',
        ),
        migrations.DeleteModel(
            name='FormPage',
        ),
    ]
