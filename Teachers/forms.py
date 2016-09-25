from django import forms


from .models import Teacher

class PostForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = [
            "name",
            "slug",
            "sex",
            "image",
            "height_field", 
            "width_field", 
            "professional_title",
            "address",
            "college",
            "academy",
            "institution",
            "post_number",
            "phone_number",
            "mail",
            "content", 
            "UG_lesson",
            "PG_lesson",
            "research_direction",
            "research",
            "hold_project",
            "papers",           
            "books",
            "conference_papers",
            "recruitment",
        ]
