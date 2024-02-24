#!/usr/bin/env bash

NAME=$1
ISO=$2

sudo virt-install \
  --virt-type kvm \
  --name "${NAME}" \
  --cdrom "${ISO}" \
  --os-variant archlinux \
  --network network=default \
  --vcpus 2 \
  --graphics vnc,listen=0.0.0.0 \
  --noautoconsole \
  --cpu host \
  --disk size=100 \
  --memory 2048
