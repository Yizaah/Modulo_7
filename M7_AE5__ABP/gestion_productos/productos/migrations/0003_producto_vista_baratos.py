from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0002_alter_producto_nombre'),
    ]

    operations = [
        migrations.RunSQL(
            """
            CREATE VIEW IF NOT EXISTS productos_baratos AS
            SELECT id, nombre, precio, disponible
            FROM productos_producto
            WHERE precio < 100;
            """
        )
    ]