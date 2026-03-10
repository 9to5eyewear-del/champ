import importlib.util

# טעינת dash.py כקובץ נסתר (לא import סטנדרטי)
_spec = importlib.util.spec_from_file_location("_dash", "dash.py")
_dash = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_dash)

print("Hello, World!")
