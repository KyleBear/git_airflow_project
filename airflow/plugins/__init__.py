# # airflow_plugins/__init__.py

# import pkgutil
# import importlib
# from airflow.plugins_manager import AirflowPlugin
# import os
# # 현재 패키지 디렉토리
# # package_dir = __file__.rsplit('/', 1)[0]
# package_dir = os.path.dirname(__file__)


# # 플러그인 클래스 정의
# class AutoRegisterPlugin(AirflowPlugin):
#     name = "auto_register_plugin"
    
#     def __init__(self):
#         self.operators = []
#         self.sensors = []
#         self.hooks = []
#         self._load_plugins()

#     def _load_plugins(self):
#         # 디렉토리 내의 모든 모듈을 탐색하여 자동으로 등록합니다.
#         for loader, module_name, is_pkg in pkgutil.iter_modules([package_dir]):
#             if is_pkg:
#                 continue
#             module = importlib.import_module(f'airflow_plugins.{module_name}')
            
#             # 모듈에서 `Operator`, `Sensor`, `Hook` 클래스를 탐지하고 등록합니다.
#             for attr in dir(module):
#                 obj = getattr(module, attr)
#                 if isinstance(obj, type):
#                     if issubclass(obj, AirflowPlugin):
#                         if hasattr(obj, 'name'):
#                             self.operators.append(obj) if hasattr(obj, 'execute') else None
#                             self.sensors.append(obj) if hasattr(obj, 'poke') else None
#                             self.hooks.append(obj) if hasattr(obj, 'get_conn') else None

# # 플러그인 인스턴스 생성
# plugin_instance = AutoRegisterPlugin()
