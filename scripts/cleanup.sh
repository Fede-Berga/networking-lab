#!/bin/bash

# scripts/cleanup.sh
# Rimuove tutti i container e le reti del laboratorio.

echo "Pulizia in corso..."

# Ferma e rimuovi tutti i container
incus stop --all
incus delete --force router web-server workstation database guest 2>/dev/null

# Rimuovi le reti
incus network delete br-lab 2>/dev/null
incus network delete vlan-bridge 2>/dev/null
incus network delete dmz-net 2>/dev/null
incus network delete internal-net 2>/dev/null
incus network delete backend-net 2>/dev/null

# Rimuovi i profili
incus profile delete gateway-profile 2>/dev/null
incus profile delete dmz-profile 2>/dev/null
incus profile delete db-profile 2>/dev/null
incus profile delete internal-profile 2>/dev/null

echo "Tabula rasa. Il laboratorio è pulito."
