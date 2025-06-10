---
title: smoltcp support RTO
date: 2025-04-28T11:35:41.496Z
extra:
  featured: true
  link: https://github.com/BiorelaxA/smoltcp
taxonomies:
  tags:
    - OS
    - Network
---
## examplesbenchmarkrs
# smoltcp

[![docs.rs](https://docs.rs/smoltcp/badge.svg)](https://docs.rs/smoltcp)
[![crates.io](https://img.shields.io/crates/v/smoltcp.svg)](https://crates.io/crates/smoltcp)
[![crates.io](https://img.shields.io/crates/d/smoltcp.svg)](https://crates.io/crates/smoltcp)
[![crates.io](https://img.shields.io/matrix/smoltcp:matrix.org)](https://matrix.to/#/#smoltcp:matrix.org)
[![codecov](https://codecov.io/github/smoltcp-rs/smoltcp/branch/master/graph/badge.svg?token=3KbAR9xH1t)](https://codecov.io/github/smoltcp-rs/smoltcp)

_smoltcp_ is a standalone, event-driven TCP/IP stack that is designed for bare-metal,
real-time systems. Its design goals are simplicity and robustness. Its design anti-goals
include complicated compile-time computations, such as macro or type tricks, even
at cost of performance degradation.

_smoltcp_ does not need heap allocation *at all*, is [extensively documented][docs],
and compiles on stable Rust 1.65 and later.

_smoltcp_ achieves [~Gbps of throughput](#examplesbenchmarkrs) when tested against
the Linux TCP stack in loopback mode.

[docs]: https://docs.rs/smoltcp/

## Features

_smoltcp_ is missing many widely deployed features, usually because no one implemented them yet.
To set expectations right, both implemented and omitted features are listed.

### Media layer

There are 3 supported mediums.

* Ethernet
  * Regular Ethernet II frames are supported.
  * Unicast, broadcast and multicast packets are supported.
  * ARP packets (including gratuitous requests and replies) are supported.
  * ARP requests are sent at a rate not exceeding one per second.
  * Cached ARP entries expire after one minute.
  * 802.3 frames and 802.1Q are **not** supported.
  * Jumbo frames are **not** supported.
* IP
  * Unicast, broadcast and multicast packets are supported.
* IEEE 802.15.4
  * Only support for data frames.

### IP layer

#### IPv4

  * IPv4 header checksum is generated and validated.
  * IPv4 time-to-live value is configurable per socket, set to 64 by default.
  * IPv4 default gateway is supported.
  * Routing outgoing IPv4 packets is supported, through a default gateway or a CIDR route table.
  * IPv4 fragmentation and reassembly is supported.
  * IPv4 options are **not** supported and are silently ignored.

#### IPv6

  * IPv6 hop-limit value is configurable per socket, set to 64 by default.
  * Routing outgoing IPv6 packets is supported, through a default gateway or a CIDR route table.
  * IPv6 hop-by-hop header is supported.
  * ICMPv6 parameter problem message is generated in response to an unrecognized IPv6 next header.
  * ICMPv6 parameter problem message is **not** generated in response to an unknown IPv6
    hop-by-hop option.

#### 6LoWPAN

  * Implementation of [RFC6282](https://tools.ietf.org/rfc/rfc6282.txt).
  * Fragmentation is supported, as defined in [RFC4944](https://tools.ietf.org/rfc/rfc4944.txt).
  * UDP header compression/decompression is supported.
  * Extension header compression/decompression is supported.
  * Uncompressed IPv6 Extension Headers are **not** supported.

### IP multicast

#### IGMP

The IGMPv1 and IGMPv2 protocols are supported, and IPv4 multicast is available.

  * Membership reports are sent in response to membership queries at
    equal intervals equal to the maximum response time divided by the
    number of groups to be reported.

### ICMP layer

#### ICMPv4

The ICMPv4 protocol is supported, and ICMP sockets are available.

  * ICMPv4 header checksum is supported.
  * ICMPv4 echo replies are generated in response to echo requests.
  * ICMP sockets can listen to ICMPv4 Port Unreachable messages, or any ICMPv4 messages with
    a given IPv4 identifier field.
  * ICMPv4 protocol unreachable messages are **not** passed to higher layers when received.
  * ICMPv4 parameter problem messages are **not** generated.

#### ICMPv6

The ICMPv6 protocol is supported, and ICMP sockets are available.

  * ICMPv6 header checksum is supported.
  * ICMPv6 echo replies are generated in response to echo requests.
  * ICMPv6 protocol unreachable messages are **not** passed to higher layers when received.

#### NDISC

  * Neighbor Advertisement messages are generated in response to Neighbor Solicitations.
  * Router Advertisement messages are **not** generated or read.
  * Router Solicitation messages are **not** generated or read.
  * Redirected Header messages are **not** generated or read.

### UDP layer

The UDP protocol is supported over IPv4 and IPv6, and UDP sockets are available.

  * Header checksum is always generated and validated.
  * In response to a packet arriving at a port without a listening socket,
    an ICMP destination unreachable message is generated.

### TCP layer

The TCP protocol is supported over IPv4 and IPv6, and server and client TCP sockets are available.

  * Header checksum is generated and validated.
  * Maximum segment size is negotiated.
  * Window scaling is negotiated.
  * Multiple packets are transmitted without waiting for an acknowledgement.
  * Reassembly of out-of-order segments is supported, with no more than 4 or 32 gaps in sequence space.
  * Keep-alive packets may be sent at a configurable interval.
  * Retransmission timeout starts at at an estimate of RTT, and doubles every time.
  * Time-wait timeout has a fixed interval of 10 s.
  * User timeout has a configurable interval.
  * Delayed acknowledgements are supported, with configurable delay.
  * Nagle's algorithm is implemented.
  * Selective acknowledgements are **not** implemented.
  * Silly window syndrome avoidance is **not** implemented.
  * Congestion control is **not** implemented.
  * Timestamping is **not** supported.
  * Urgent pointer is **ignored**.
  * Probing Zero Windows is **not** implemented.
  * Packetization Layer Path MTU Discovery [PLPMTU](https://tools.ietf.org/rfc/rfc4821.txt) is **not** implemented.

## Installation

To use the _smoltcp_ library in your project, add the following to `Cargo.toml`:

```toml
[dependencies]
smoltcp = "0.10.0"
```

The default configuration assumes a hosted environment, for ease of evaluation.
You probably want to disable default features and configure them one by one:

```toml
[dependencies]
smoltcp = { version = "0.10.0", default-features = false, features = ["log"] }
```

## Feature flags

### Feature `std`

The `std` feature enables use of objects and slices owned by the networking stack through a
dependency on `std::boxed::Box` and `std::vec::Vec`.

This feature is enabled by default.

### Feature `alloc`

The `alloc` feature enables use of objects owned by the networking stack through a dependency
on collections from the `alloc` crate. This only works on nightly rustc.

This feature is disabled by default.

### Feature `log`

The `log` feature enables logging of events within the networking stack through
the [log crate][log]. Normal events (e.g. buffer level or TCP state changes) are emitted with
the TRACE log level. Exceptional events (e.g. malformed packets) are emitted with
the DEBUG log level.

[log]: https://crates.io/crates/log

This feature is enabled by default.

### Feature `defmt`

The `defmt` feature enables logging of events with the [defmt crate][defmt].

[defmt]: https://crates.io/crates/defmt

This feature is disabled by default, and cannot be used at the same time as `log`.

### Feature `verbose`

The `verbose` feature enables logging of events where the logging itself may incur very high
overhead. For example, emitting a log line every time an application reads or writes as little
as 1 octet from a socket is likely to overwhelm the application logic unless a `BufReader`
or `BufWriter` is used, which are of course not available on heap-less systems.

This feature is disabled by default.

### Features `phy-raw_socket` and `phy-tuntap_interface`

Enable `smoltcp::phy::RawSocket` and `smoltcp::phy::TunTapInterface`, respectively.

These features are enabled by default.

### Features `socket-raw`, `socket-udp`, `socket-tcp`, `socket-icmp`, `socket-dhcpv4`, `socket-dns`

Enable the corresponding socket type.

These features are enabled by default.

### Features `proto-ipv4`, `proto-ipv6` and `proto-sixlowpan`

Enable [IPv4], [IPv6] and [6LoWPAN] respectively.

[IPv4]: https://tools.ietf.org/rfc/rfc791.txt
[IPv6]: https://tools.ietf.org/rfc/rfc8200.txt
[6LoWPAN]: https://tools.ietf.org/rfc/rfc6282.txt