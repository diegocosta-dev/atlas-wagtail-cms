# Generated by Django 5.1.7 on 2025-03-20 14:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_rename_hero_cta_link_homepage_hero_cta_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='homepage',
            old_name='hero_cta_label',
            new_name='cta_label',
        ),
        migrations.RenameField(
            model_name='homepage',
            old_name='hero_cta_page',
            new_name='cta_page',
        ),
        migrations.RenameField(
            model_name='homepage',
            old_name='hero_cta_url',
            new_name='cta_url',
        ),
        migrations.RenameField(
            model_name='homepage',
            old_name='hero_heading',
            new_name='heading',
        ),
        migrations.RenameField(
            model_name='homepage',
            old_name='author_image',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='homepage',
            old_name='hero_summary',
            new_name='summary',
        ),
    ]
