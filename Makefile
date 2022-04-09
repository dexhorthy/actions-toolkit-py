.PHONY: test
test:
	cd actions_toolkit && python -m unittest
test-image:
	docker build -t test .
	docker run test "echo 'print(\"hi\")' >> /work/script.py && /work/script.py"
