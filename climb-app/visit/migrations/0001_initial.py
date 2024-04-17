# Generated by Django 5.0.4 on 2024-04-11 08:08

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Visitor",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("birth", models.CharField(max_length=10, verbose_name="생년월일")),
                (
                    "gender",
                    models.CharField(
                        choices=[("M", "남자"), ("W", "여자"), ("X", "선택안함")],
                        default="X",
                        max_length=2,
                        verbose_name="성별",
                    ),
                ),
                ("name", models.CharField(max_length=30, verbose_name="이름")),
                (
                    "address",
                    models.CharField(
                        blank=True, max_length=150, null=True, verbose_name="주소"
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="생성 날짜"),
                ),
            ],
            options={
                "verbose_name": "일일권 방문자",
                "verbose_name_plural": "일일권 방문자",
            },
        ),
    ]
