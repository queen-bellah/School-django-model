# Generated by Django 5.0.6 on 2024-08-09 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("course", "0002_courses_delete_course"),
        ("student", "0004_remove_student_gender_remove_student_guardian"),
    ]

    operations = [
        migrations.AddField(
            model_name="student",
            name="course",
            field=models.ManyToManyField(to="course.courses"),
        ),
    ]
