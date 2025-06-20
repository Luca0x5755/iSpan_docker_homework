# docker 作業 / 大專框架

```sh
# 使用 docker-compose.yml
docker compose up
```

## 使用自簽憑證

1. 在ubuntu中執行 generate-cert.sh
2. 將產生出來的`certs`資料夾放置在專案內的`nginx`資料夾內

```sh
source generate-cert.sh
```

TODO: 需要改成能夠方便開發的模式
