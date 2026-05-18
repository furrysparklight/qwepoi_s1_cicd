# my first ci/cd
## create project
- fastapi
- caddy
## create Dockerfile
## create docker-compose.yml
## create the Action
- create action
- configure action

## Todo:
- add 2nd workflow yml to dev branch
- add watchtower config to 2nd run
- add back full docker compose stack with Caddy to serve behind nginx reverse proxy

## notes
### action logic issues:
- in 'push:' section conditions are working as OR:
thus it fires ON ANY OF Tag or Branch matching case
  push:
    branches:
      - 'main'      # Сборка при пуше в main
      - 'dev'       # Сборка при пуше в dev
    tags:
      - 'v*.*'       # Включает v2.7, v2.7-beta
      - '!v*.*.*'    # ИСКЛЮЧАЕТ v2.7.1, v2.7-beta.14 (если там 3 сегмента через точку)

      
- use IF condition in build section:
on:
  workflow_dispatch: # Магическая кнопка ручного запуска
  push:
    tags:
      - 'v*.*'       # Включает v2.7, v2.7-beta
      - '!v*.*.*'    # ИСКЛЮЧАЕТ патчи вроде v2.7.1

jobs:
  build-and-push:
    runs-on: ubuntu-latest
    # СТРОГОЕ УСЛОВИЕ (AND): Запускать только если это ручной запуск ИЛИ тег был пушнут именно в ветку main
    if: |
      github.event_name == 'workflow_dispatch' || 
      (github.event_name == 'push' && github.event.base_ref == 'refs/heads/main')