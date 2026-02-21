from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

from app.models import User


def generate_user_pdf(user: User) -> BytesIO:
    buffer = BytesIO()

    p = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter

    p.drawString(100, height - 100, f"User Profile")
    p.drawString(100, height - 130, f"ID: {user.id}")
    p.drawString(100, height - 150, f"Name: {user.name}")
    p.drawString(100, height - 170, f"Surname: {user.surname}")
    p.drawString(100, height - 190, f"Email: {user.email}")
    p.drawString(100, height - 210, f"Date of birth: {user.date_of_birth}")

    p.showPage()
    p.save()

    buffer.seek(0)
    return buffer
