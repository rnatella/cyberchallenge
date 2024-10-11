# prepare environment
prepare:
	docker info >/dev/null 2>/dev/null
	@sudo iptables -L DOCKER-USER | grep "ACCEPT     all" >/dev/null 2>&1 || sudo iptables -I DOCKER-USER -j ACCEPT
	@sudo ./net.sh add
	@echo "Environment created."

clean:
	-sudo iptables -L DOCKER-USER | grep "ACCEPT     all" >/dev/null 2>&1 && sudo iptables -D DOCKER-USER -j ACCEPT
	-sudo ./net.sh del

up:	prepare
	docker network prune -f
	docker-compose up -d

stop:
	docker-compose stop

down:
	docker-compose down

logs:
	docker-compose logs -f
