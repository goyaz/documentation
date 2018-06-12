%global commit0 8171917609dfd0a331a8460d16ded7bba6334e15

Name:           php-LC-openvpn-connection-manager
Version:        1.0.1
Release:        1%{?dist}
Summary:        Manage client connections to OpenVPN processes

License:        MIT
URL:            https://git.tuxed.net/LC/php-openvpn-connection-manager
Source0:        https://git.tuxed.net/LC/php-openvpn-connection-manager/snapshot/php-openvpn-connection-manager-%{commit0}.tar.xz

BuildArch:      noarch

#        "php": ">=5.4",
BuildRequires:  php(language) >= 5.4.0
#        "psr/log": "^1.0",
BuildRequires:  php-composer(psr/log)
BuildRequires:  %{_bindir}/phpab
BuildRequires:  %{_bindir}/phpunit

#        "php": ">=5.4",
Requires:       php(language) >= 5.4.0
#        "psr/log": "^1.0",
Requires:       php-composer(psr/log)

Provides:       php-composer(LC/openvpn-connection-manager) = %{version}

%description
Simple library written in PHP to manage client connections to OpenVPN processes 
through the OpenVPN management socket.

%prep
%autosetup -n php-openvpn-connection-manager-%{commit0}

%build
%{_bindir}/phpab -o src/autoload.php src
cat <<'AUTOLOAD' | tee -a src/autoload.php
require_once '%{_datadir}/php/Psr/Log/autoload.php';
AUTOLOAD

%install
mkdir -p %{buildroot}%{_datadir}/php/LC/OpenVpn
cp -pr src/* %{buildroot}%{_datadir}/php/LC/OpenVpn

%check
%{_bindir}/phpab -o tests/autoload.php tests
cat <<'AUTOLOAD' | tee -a tests/autoload.php
require_once 'src/autoload.php';
AUTOLOAD

%{_bindir}/phpunit tests --verbose --bootstrap=tests/autoload.php

%files
%license LICENSE
%doc composer.json CHANGES.md README.md
%dir %{_datadir}/php/LC
%{_datadir}/php/LC/OpenVpn

%changelog
* Thu Jun 07 2018 François Kooman <fkooman@tuxed.net> - 1.0.1-1
- update to 1.0.1

* Wed Jun 06 2018 François Kooman <fkooman@tuxed.net> - 1.0.0-2
- update upstream source URL

* Tue Jun 05 2018 François Kooman <fkooman@tuxed.net> - 1.0.0-1
- initial package