#global git 2f5c4770a76cf1f4c913a35977108314b3af9ade

Name:           php-fkooman-otp-verifier
Version:        0.2.0
Release:        6%{?dist}
Summary:        OTP Verification Library

License:        MIT
URL:            https://software.tuxed.net/php-otp-verifier
%if %{defined git}
Source0:        https://git.tuxed.net/fkooman/php-otp-verifier/snapshot/php-otp-verifier-%{git}.tar.xz
%else
Source0:        https://software.tuxed.net/php-otp-verifier/files/php-otp-verifier-%{version}.tar.xz
Source1:        https://software.tuxed.net/php-otp-verifier/files/php-otp-verifier-%{version}.tar.xz.asc
Source2:        gpgkey-6237BAF1418A907DAA98EAA79C5EDD645A571EB2
%endif

BuildArch:      noarch

BuildRequires:  gnupg2
BuildRequires:  php-fedora-autoloader-devel
BuildRequires:  %{_bindir}/phpab
#    "require-dev": {
#        "phpunit/phpunit": "^4|^5|^6|^7",
#    },
%if 0%{?fedora} >= 28 || 0%{?rhel} >= 8
BuildRequires:  phpunit7
%global phpunit %{_bindir}/phpunit7
%else
BuildRequires:  phpunit
%global phpunit %{_bindir}/phpunit
%endif
#    "require": {
#        "ext-date": "*",
#        "ext-hash": "*",
#        "ext-pdo": "*",
#        "ext-spl": "*",
#        "paragonie/constant_time_encoding": "^1|^2",
#        "paragonie/random_compat": ">=1",
#        "php": ">= 5.4",
#        "symfony/polyfill-php56": "^1"
#    },
BuildRequires:  php(language) >= 5.4.0
BuildRequires:  php-date
BuildRequires:  php-hash
BuildRequires:  php-pdo
BuildRequires:  php-spl
BuildRequires:  php-composer(paragonie/constant_time_encoding)
%if 0%{?fedora} < 28 && 0%{?rhel} < 8
BuildRequires:  php-composer(paragonie/random_compat)
BuildRequires:  php-composer(symfony/polyfill-php56)
%endif

#    "require": {
#        "ext-date": "*",
#        "ext-hash": "*",
#        "ext-pdo": "*",
#        "ext-spl": "*",
#        "paragonie/constant_time_encoding": "^1|^2",
#        "paragonie/random_compat": ">=1",
#        "php": ">= 5.4",
#        "symfony/polyfill-php56": "^1"
#    },
Requires:       php(language) >= 5.4.0
Requires:       php-date
Requires:       php-hash
Requires:       php-pdo
Requires:       php-spl
Requires:       php-composer(paragonie/constant_time_encoding)
%if 0%{?fedora} < 28 && 0%{?rhel} < 8
Requires:       php-composer(paragonie/random_compat)
Requires:       php-composer(symfony/polyfill-php56)
%endif

Provides:       php-composer(fkooman/otp-verifier) = %{version}

%description
OTP Verification Library.

%prep
%if %{defined git}
%autosetup -n php-otp-verifier-%{git}
%else
gpgv2 --keyring %{SOURCE2} %{SOURCE1} %{SOURCE0}
%autosetup -n php-otp-verifier-%{version}
%endif

%build
%{_bindir}/phpab -t fedora -o src/autoload.php src
cat <<'AUTOLOAD' | tee -a src/autoload.php
require_once '%{_datadir}/php/ParagonIE/ConstantTime/autoload.php';
AUTOLOAD
%if 0%{?fedora} < 28 && 0%{?rhel} < 8
cat <<'AUTOLOAD' | tee -a src/autoload.php
require_once '%{_datadir}/php/random_compat/autoload.php';
require_once '%{_datadir}/php/Symfony/Polyfill/autoload.php';
AUTOLOAD
%endif

%install
mkdir -p %{buildroot}%{_datadir}/php/fkooman/Otp
cp -pr src/* %{buildroot}%{_datadir}/php/fkooman/Otp

%check
%{_bindir}/phpab -o tests/autoload.php tests
cat <<'AUTOLOAD' | tee -a tests/autoload.php
require_once 'src/autoload.php';
AUTOLOAD

%{phpunit} tests --verbose --bootstrap=tests/autoload.php

%files
%license LICENSE
%doc composer.json CHANGES.md README.md
%dir %{_datadir}/php/fkooman
%{_datadir}/php/fkooman/Otp

%changelog
* Sun Sep 09 2018 François Kooman <fkooman@tuxed.net> - 0.2.0-6
- merge dev and prod spec files in one
- cleanup requirements

* Sat Sep 08 2018 François Kooman <fkooman@tuxed.net> - 0.2.0-5
- only autoload compat libraries on older versions of Fedora/EL

* Sun Aug 05 2018 François Kooman <fkooman@tuxed.net> - 0.2.0-4
- use phpunit7 on supported platforms

* Mon Jul 23 2018 François Kooman <fkooman@tuxed.net> - 0.2.0-3
- add missing BR

* Mon Jul 23 2018 François Kooman <fkooman@tuxed.net> - 0.2.0-2
- use fedora phpab template for generating autoloader

* Fri Jul 20 2018 François Kooman <fkooman@tuxed.net> - 0.2.0-1
- initial package
