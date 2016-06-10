Name: jolokia-jvm-agent		
Version: 1.3.3
Release: 1%{?dist}
Summary: Jolokia is remote JMX with JSON over HTTP
Group: Applications/Internet
License: Apache (v2)
URL: https://jolokia.org/
Source0: https://github.com/rhuss/jolokia/releases/download/v1.3.3/jolokia-1.3.3-source.tar.gz
BuildArch: noarch
BuildRequires: java, maven
Requires: java
Packager: Heikki Nousiainen <htn@aiven.io>

%description
Jolokia is a JMX-HTTP bridge giving an alternative to JSR-160 connectors. It is an agent based approach with support for many platforms. In addition to basic JMX operations it enhances JMX remoting with unique features like bulk requests and fine grained security policies.

%prep
%setup -n jolokia-%{version}

%build
mvn package

%install
%{__mkdir_p} %{buildroot}/opt/jolokia-jvm-agent-%{version}
install agent/jvm/target/jolokia-jvm-%{version}-agent.jar %{buildroot}/opt/jolokia-jvm-agent-%{version}/jolokia-jvm-%{version}-agent.jar

%files
/opt/jolokia-jvm-agent-%{version}

%changelog
* Fri Jun 10 2016 Heikki Nousiainen <htn@aiven.io>
- First build
