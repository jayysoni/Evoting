#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

def main():
    """Run administrative tasks."""
    
    # Ensure the virtual environment is activated
    if not os.getenv('VIRTUAL_ENV'):
        print("⚠️ Warning: No virtual environment detected! Make sure to activate it.")

    # Set the default settings module for Django
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'evoting.settings')
    
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    
    # Execute Django command-line utility
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()