#!/bin/bash

DEV="ccit-net"

case $1 in
"add")
  sudo ip link show $DEV || sudo ip link add $DEV type dummy
  sudo ip link set dev $DEV up
  ;;
"del")
  sudo ip link show $DEV && sudo ip link del $DEV type dummy
  ;;
*)
  echo "$0 [add|del]"
  ;;
esac
