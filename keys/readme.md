# Flipper clone CKS区域的密钥

## U2F

在U2F文件夹中，编译固件时替换 applications/main/u2f/resources/u2f/assets 文件夹中的 cert.der 和 cert_key.u2f。

## Firmware_file

在Firmware_file文件夹中，编译固件时替换targets/f7/furi_hal/furi_hal_crypto.c

## 密钥（CKS区域的内容）

密钥需要在刷写Core fus后通过dfu mode刷入（STM32CubeProgrammer）。

密钥文件 keyX.bin，对应了key_slot 1-10。

密钥位置定义：

| 槽位编号 | 保存的内容/用途 |
| --- | --- |
| 0 | Master Key，用于加密剩余所有槽位的密钥 |
| 1 | Keeloq 协议实现所使用的，数据处理加密密钥 |
| 2 | U2F 功能所使用的，配合证书使用的密钥 |
| 3 | / |
| 4 | / |
| 5 | / |
| 6 | / |
| 7 | / |
| 8 | / |
| 9 | / |
| 10 | / |
| 11 | 常规情况下的 FURI_HAL_CRYPTO_ENCLAVE_UNIQUE_KEY_SLOT，由 Flipper Zero 自动生成 |

## 相关

[shilapi的博客](https://www.lapiw.icu/flipper_zero_cks_u2f)