---
title: "Generate a key"
layout: keygen
lead: "Give your repeater a prefix that no repeater near you uses. Find a free prefix, make a key that starts with it, and set it."
description: "Make a MeshCore key with a prefix you choose, in your browser, so no repeater near yours shares its prefix in a path."
---

A repeater passes messages on for everyone around it. In a path, MeshCore
names each repeater by the first bytes of its public key:
its prefix. When a repeater near you has the same prefix, a path does not show
which of the two passed a message on. MeshCore picks the key at random. Here
you make one with the prefix you want.

Take 2 bytes. On 13 October 2026 the [MeshCore Analyzer](https://meshcore-analyzer.eu/)
saw every 1-byte prefix shared in Europe. The path hash size, a setting of
the sender, decides how many bytes of each prefix go into a path; see [CLI commands](/guides/cli/).
