.PHONY: help revision upgrade downgrade crurrent history shell


COMPOSE_FILE = ../../docker/docker-compose.dev.yml
COMPOSE = docker compose -f $(COMPOSE_FILE)
SERVICE = backend

ALEMBIC=$(COMPOSE) exec $(SERVICE) alembic -c app/alembic.ini

help:
	@echo "Available commands:"
	@echo " make revision m='message'	- create new migration"
	@echo " make upgrade                - upgrade to head"
	@echo " make downgrade r=revision   - downgrade to revision"
	@echo " make current                - show current revision"
	@echo " make history                - show migration history"

revision:
	@if [ -z "$(m)" ]; then echo "Migration message is required: make revision m='message'"; exit 1; fi
	$(ALEMBIC) revision --autogenerate -m "$(m)"


upgrade:
	$(ALEMBIC) upgrade head

downgrade:
	@if [ -z "$(r)"]; then echo "Revision is required: make downgrade r=revision_id"; exit 1; fi
	$(ALEMBIC) downgrade $(r)

current:
	$(ALEMBIC) 	current

history:
	$(ALEMBIC) 	history

shell:
	$(COMPOSE) exec $(SERVICE) sh