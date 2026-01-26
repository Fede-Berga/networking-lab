# Lab di Networking: Guida alla Struttura

Questo progetto è organizzato per supportare una lezione strutturata sulla segmentazione di rete.

## 📁 Struttura Cartelle
- `lesson-plan.md`: La guida dettagliata passo-passo per il docente e gli studenti.
- `scripts/`:
    - `setup_incus.sh`: Configura il bridge VLAN iniziale.
    - `deploy_lab.sh`: Esegue il deploy automatico del laboratorio (Part 2 - VLAN).
    - `cleanup.sh`: Rimuove tutto il laboratorio per ricominciare.
- `config/`:
    - `gateway_firewall.nft`: Regole di sicurezza per il router.
- `app/`:
    - `app.py`: Esempio di applicazione web per il test del Layer 7.

## 🚀 Come Iniziare
1. **Configurazione ambiente**: Segui le istruzioni per il tuo OS nel `lesson-plan.md`.
2. **Esecuzione Lab**:
   ```bash
   bash scripts/setup_incus.sh
   bash scripts/deploy_lab.sh
   ```
3. **Pulizia**:
   ```bash
   bash scripts/scripts/cleanup.sh
   ```

## 🎯 Obiettivi Didattici
Il laboratorio è diviso in tre fasi:
1. **Ponti Fisici**: Capire la separazione fisica tra reti.
2. **VLAN (802.1Q)**: Migrare verso la segmentazione logica su un singolo cavo (Trunk).
3. **Firewalling**: Proteggere i segmenti con regole di accesso granulari.
