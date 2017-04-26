Name: jolokia-jvm-agent		
Version: 1.3.6
Release: 1%{?dist}
Summary: Jolokia is remote JMX with JSON over HTTP
Group: Applications/Internet
License: Apache (v2)
URL: https://jolokia.org/
Source0: https://github.com/rhuss/jolokia/releases/download/v%{version}/jolokia-%{version}-source.tar.gz
BuildArch: noarch
BuildRequires: java
%if 0%{?rhel} >= 7
BuildRequires: maven
%else
BuildRequires: apache-maven
%endif
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
* Wed Apr 26 2017 Matt Dainty <matt@bodgit-n-scarper.com>
- Bump to v1.3.6
- Handle building on EL6 using the dchen repository for Maven packages

* Fri Jun 10 2016 Heikki Nousiainen <htn@aiven.io>
- First build
