Name:    patito-release
Version: 1
Release: 1%{?dist}
Summary: patito.club yum repository

License: Public Domain
Source0: patito.repo
BuildArch: noarch

%description
patito.club yum repository config file

%install
mkdir -p %{buildroot}/etc/yum.repos.d
install -p -m 755 %{SOURCE0} %{buildroot}/etc/yum.repos.d

%files

%changelog
