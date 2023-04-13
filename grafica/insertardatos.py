from tabla.models import Alumnos

alumno1 = Alumnos(id=1, nombre='Diego', apellido='Figueroa', horas=10)
alumno1.save()

alumno2 = Alumnos(id=2, nombre='Pablo', apellido='Sanchez', horas=25)
alumno2.save()

alumno3 = Alumnos(id=3, nombre='Carolina', apellido='Gonzalez', horas=30)
alumno3.save()

alumno4 = Alumnos(id=4, nombre='Sergio', apellido='Ruiz', horas=15)
alumno4.save()

alumno5 = Alumnos(id=5, nombre='Luis Jose', apellido='Gonzalez', horas=38)
alumno5.save()

alumno6 = Alumnos(id=6, nombre='Christian', apellido='Vallejo', horas=23)
alumno6.save()