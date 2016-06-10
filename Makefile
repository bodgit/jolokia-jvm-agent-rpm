all: rpm

rpm:
	rpmbuild -bb jolokia-jvm-agent.spec
