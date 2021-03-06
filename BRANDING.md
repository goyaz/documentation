This document describes how to add the Let's Connect! or eduVPN branding to 
your server installation. By default a simple "plain" branding is used.

# Installation

## CentOS 

    $ sudo yum -y install vpn-portal-artwork-LC
    $ sudo yum -y install vpn-portal-artwork-eduVPN

## Fedora

    $ sudo dnf -y install vpn-portal-artwork-LC
    $ sudo dnf -y install vpn-portal-artwork-eduVPN

## Debian

    $ sudo apt-get -y install vpn-portal-artwork-lc
    $ sudo apt-get -y install vpn-portal-artwork-eduvpn

# Configuration

Now you can enable the `styleName` in `/etc/vpn-user-portal/default/config.php` 
and `/etc/vpn-admin-portal/default/config.php`. Set it to `LC` (or `eduVPN`).

For `vpn-admin-portal` you can also configure the color of the bar graphs on
the "Stats" page.

    'statsConfig' => [
        'barColor' => [0x11, 0x93, 0xf5], // Let's Connect Blue
        //'barColor' => [0xdf, 0x7f, 0x0c], // eduVPN orange
    ],

After finishing the configuration, make sure you wipe the template cache:

    $ sudo rm -rf /var/lib/vpn-user-portal/default/tpl
    $ sudo rm -rf /var/lib/vpn-admin-portal/default/tpl
