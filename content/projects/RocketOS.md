---
title: RocketOS
date: 2025-02-11T11:35:41.496Z
extra:
  featured: true
  link: https://github.com/BiorelaxA/RocketOS
description: "An open-source neural language technology platform supporting
  six   fundamental Chinese NLP tasks: <ul>   <li>lexical analysis (Chinese word
  segmentation,   part-of-speech tagging, and named entity
  recognition)</li>   <li>syntactic parsing   (dependency
  parsing)</li>   <li>semantic parsing (semantic dependency parsing
  and   semantic role labeling)</li> </ul>"
taxonomies:
  tags:
    - Rust
    - OS
---
<p align="center">RocketOS - Rust RISC-V Operating System</p>

<p align="center">
RocketOS is a simple operating system which is written in RUST and Assembly.
</p>

<p align="center">
  <a title="Rustc Version" target="_blank" href="https://www.rust-lang.org/"><img alt="Rustc Version" src="https://img.shields.io/badge/Rustc-%3E%3D%201.82.0-orange?style=flat"></a>
  <a title="License" target="_blank" href="https://github.com/li041/RROS/blob/main/LICENSE"><img alt="License" src="https://img.shields.io/github/license/li041/RROS.svg?style=flat"></a>
  <br>
  <a title="GitHub Release" target="_blank" href="https://github.com/li041/RROS/releases"><img alt="GitHub Release" src="https://img.shields.io/github/v/release/li041/RROS?style=flat"></a>
  <a title="GitHub Commits" target="_blank" href="https://github.com/li041/RROS/commits/main"><img alt="GitHub Commits" src="https://img.shields.io/github/commit-activity/m/li041/RROS.svg?style=flat&color=brightgreen&label=commits"></a>
  <br><br>
  <a title="GitHub Watchers" target="_blank" href="https://github.com/li041/RROS/watchers"><img alt="GitHub Watchers" src="https://img.shields.io/github/watchers/li041/RROS.svg?label=Watchers&style=social"></a>  
  <a title="GitHub Stars" target="_blank" href="https://github.com/li041/RROS/stargazers"><img alt="GitHub Stars" src="https://img.shields.io/github/stars/li041/RROS.svg?label=Stars&style=social"></a>  
  <a title="GitHub Forks" target="_blank" href="https://github.com/li041/RROS/network/members"><img alt="GitHub Forks" src="https://img.shields.io/github/forks/li041/RROS.svg?label=Forks&style=social"></a>  
</p>

## 🎯 Quick Start

To get started with RROS, follow the steps below:

1. **Clone the repository**

```bash
git clone https://github.com/li041/RROS.git
cd RROS
##Make sure you have Rust 1.82.0 or higher installed:
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
rustup update stable
```
   
2. **Build the OS**

```bash
cargo build --release
```
3. Run in QEMU

You can test RROS in the QEMU emulator:

```bash
qemu-system-riscv64 -machine virt -nographic -kernel target/riscv64gc-unknown-none-elf/release/rros
(Make sure you have QEMU installed and configured to support RISC-V)
```

## 📦 Features
Minimal RISC-V operating system kernel written in Rust and Assembly

Basic hardware initialization and interrupt handling

Memory management with page tables

Simple scheduler and multitasking support

Support for RISC-V privileged architecture

Modular design for easy extension and experimentation

Early-stage file system and device driver prototypes (work in progress)