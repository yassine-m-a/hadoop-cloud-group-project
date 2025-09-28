# Hadoop Cloud Group Project - Télécom Paris

<p align="center">
  <img src="./elephant-hadoop.jpg" alt="WAIT WHAT? YOU DON'T KNOW HADOOP?" width="500"/>
</p>

Bienvenue dans notre projet Hadoop distribué 😎 !

## Participants
Yassine MERNISSI ARIFI <br/>
Julien LAFRANCE <br/>
Omar FEKIH-HASSEN <br/>
Alexandre DONNAT <br/>

## Structure du projet

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
│   ├── hbase-master.service # Déployé sur le HManager (22) active, et le HManager standby (9)
│   ├── hbase-regionserver.service # Déployé sur les HRegionServer
│   └── zookeeper.service    # Déployé sur toutes les machines
│
└── README.md              # Ce fichier
```

## Exemples d’exécution

### Upload d’un fichier dans HDFS (via WebHDFS)
```bash
curl -i -X PUT -T /data2/Public/your_file.xml "http://tp-hadoop-22:9870/webhdfs/v1/user/ubuntu/your_file.xml?op=CREATE&overwrite=true&user.name=ubuntu" -L
```

### Exemple MapReduce sur plusieurs noeuds: calcul de π
```bash
hadoop jar /opt/hadoop/share/hadoop/mapreduce/hadoop-mapreduce-examples-*.jar pi 16 1000
```

### Exemple Hadoop Streaming : WordCount (mapper/reducer à la main en Python)
```bash
hadoop jar /opt/hadoop/share/hadoop/tools/lib/hadoop-streaming-*.jar \
  -input /user/ubuntu/wikipedia_fr_dump_17Go.xml \
  -output /user/ubuntu/output-mapper-reducer-wc \
  -mapper ~/scripts/mapper.py \
  -reducer ~/scripts/reducer.py \
  -file ~/scripts/mapper.py \
  -file ~/scripts/reducer.py
```

### Exemple PySpark : Job à travers YARN
```bash
/opt/spark/bin/spark-submit \
  --master yarn \
  --deploy-mode client \
  --num-executors 8 \
  --executor-cores 2 \
  --executor-memory 3g \
  --driver-memory 2g \
  --conf spark.sql.shuffle.partitions=16 \
  --conf spark.default.parallelism=16 \
  /home/ubuntu/scripts/pyspark_count_word.py
```
