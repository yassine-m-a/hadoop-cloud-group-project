# Hadoop Cloud Group Project - Télécom Paris

![WAIT WHAT? YOU DON'T KNOW HADOOP?](./elephant-hadoop.jpg)

Bienvenue dans notre projet Hadoop distribué 😎 !

## Participants
Yassine MERNISSI ARIFI
Julien LAFRANCE
Omar FEKIH-HASSEN
Alexandre DONNAT

## 🗂️ Structure du projet

```bash
HADOOP-CLOUD-GROUP-PROJECT/
├── config/
│   ├── hadoop/              # Configs XML pour HDFS, YARN, MapReduce
│   ├── hbase/               # Configs pour HBase 
│   ├── spark/               # Configs pour Spark
│   └── zookeeper/           # zoo.cfg (ZK quorum)
│
├── scripts/                 # Scripts Python pour MapReduce & PySpark
│   ├── yarn                 # Mapper et reducer à la main
│   └── spark                # Scripts Spark
│
├── systemd/                 # Fichiers .service pour démarrage auto
│   ├── hadoop.service       # Déployé sur le Master Node (22)
│   ├── hbase-master.service # Déployé sur le HManager (22), et le HManager standby (9)
│   └── zookeeper.service    # Déployé sur toutes les machines
│
└── README.md              # Ce fichier
