
Name: app-imap-plugin
Epoch: 1
Version: 1.4.12
Release: 1%{dist}
Summary: IMAP and POP Server Policies - Core
License: LGPLv3
Group: ClearOS/Libraries
Source: app-imap-plugin-%{version}.tar.gz
Buildarch: noarch

%description
IMAP and POP Server Policies provide access control for the IMAP and POP Server app.

%package core
Summary: IMAP and POP Server Policies - Core
Requires: app-base-core
Requires: app-accounts-core

%description core
IMAP and POP Server Policies provide access control for the IMAP and POP Server app.

This package provides the core API and libraries.

%prep
%setup -q
%build

%install
mkdir -p -m 755 %{buildroot}/usr/clearos/apps/imap_plugin
cp -r * %{buildroot}/usr/clearos/apps/imap_plugin/

install -D -m 0644 packaging/imap.php %{buildroot}/var/clearos/accounts/plugins/imap.php

%post core
logger -p local6.notice -t installer 'app-imap-plugin-core - installing'

if [ $1 -eq 1 ]; then
    [ -x /usr/clearos/apps/imap_plugin/deploy/install ] && /usr/clearos/apps/imap_plugin/deploy/install
fi

[ -x /usr/clearos/apps/imap_plugin/deploy/upgrade ] && /usr/clearos/apps/imap_plugin/deploy/upgrade

exit 0

%preun core
if [ $1 -eq 0 ]; then
    logger -p local6.notice -t installer 'app-imap-plugin-core - uninstalling'
    [ -x /usr/clearos/apps/imap_plugin/deploy/uninstall ] && /usr/clearos/apps/imap_plugin/deploy/uninstall
fi

exit 0

%files core
%defattr(-,root,root)
%exclude /usr/clearos/apps/imap_plugin/packaging
%exclude /usr/clearos/apps/imap_plugin/tests
%dir /usr/clearos/apps/imap_plugin
/usr/clearos/apps/imap_plugin/deploy
/usr/clearos/apps/imap_plugin/language
/usr/clearos/apps/imap_plugin/libraries
/var/clearos/accounts/plugins/imap.php
