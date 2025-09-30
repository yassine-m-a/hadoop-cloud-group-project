## 🚀 START SERVICES

### 🔧 tp-hadoop-22 (NameNode, Resource Manager, HMaster standby, HRegionServer, QuorumPeerMain)
```bash
sudo systemctl start hadoop hbase-master hbase-regionserver zookeeper
```
> **Note :** Le service Hadoop lance automatiquement par SSH les DataNodes / NodeManagers dans les autres machines.

### 🔧 tp-hadoop-9 (HMaster standby, HRegionServer, QuorumPeerMain)
```bash
sudo systemctl start hbase-master hbase-regionserver zookeeper
```

### 🔧 tp-hadoop-30 (HRegionServer, QuorumPeerMain)
```bash
sudo systemctl start hbase-regionserver zookeeper
```

### 🔧 tp-hadoop-31 (HRegionServer, QuorumPeerMain)
```bash
sudo systemctl start hbase-regionserver zookeeper
```

---

## 📊 CHECK SERVICES

> **Astuce :** Utilisez `jps` pour avoir une vision complète des processus Java en cours d'exécution.

### 📋 tp-hadoop-22 (NameNode, Resource Manager, HMaster standby, HRegionServer, QuorumPeerMain)
```bash
sudo systemctl status hadoop hbase-master hbase-regionserver zookeeper
```

### 📋 tp-hadoop-9 (HMaster standby, HRegionServer, QuorumPeerMain)
```bash
sudo systemctl status hbase-master hbase-regionserver zookeeper
```

### 📋 tp-hadoop-30 (HRegionServer, QuorumPeerMain)
```bash
sudo systemctl status hbase-regionserver zookeeper
```

### 📋 tp-hadoop-31 (HRegionServer, QuorumPeerMain)
```bash
sudo systemctl status hbase-regionserver zookeeper
```

---

## 🛑 STOP SERVICES

### 🔴 tp-hadoop-22 (NameNode, Resource Manager, HMaster standby, HRegionServer, QuorumPeerMain)
```bash
sudo systemctl stop hadoop hbase-master hbase-regionserver zookeeper
```

### 🔴 tp-hadoop-9 (HMaster standby, HRegionServer, QuorumPeerMain)
```bash
sudo systemctl stop hbase-master hbase-regionserver zookeeper
```

### 🔴 tp-hadoop-30 (HRegionServer, QuorumPeerMain)
```bash
sudo systemctl stop hbase-regionserver zookeeper
```

### 🔴 tp-hadoop-31 (HRegionServer, QuorumPeerMain)
```bash
sudo systemctl stop hbase-regionserver zookeeper
```