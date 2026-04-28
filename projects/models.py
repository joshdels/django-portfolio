from django.db import models


class ProjectTag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=1000, blank=True, null=True)
    image = models.ImageField(upload_to="projects", null=True, blank=True)
    is_highlight = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
    tags = models.ManyToManyField(ProjectTag, blank=True, related_name="projects")


class ProjectBlock(models.Model):
    case_study = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="blocks"
    )

    BLOCK_TYPES = [
        ("image", "Image"),
        ("text", "Text"),
        ("quote", "Quote"),
        ("heading", "Heading"),
        ("result", "Result"),
    ]

    block_type = models.CharField(max_length=20, choices=BLOCK_TYPES)
    text = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="case-study/blocks/", blank=True, null=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ["order"]
