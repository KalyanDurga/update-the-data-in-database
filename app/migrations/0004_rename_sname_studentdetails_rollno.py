# Generated by Django 4.1.7 on 2023-04-11 09:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0003_rename_teacher_name_studentdetails_teachername_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="studentdetails",
            old_name="sname",
            new_name="rollno",
        ),
    ]
