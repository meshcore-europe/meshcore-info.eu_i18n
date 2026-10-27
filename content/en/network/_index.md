---
title: "The network"
layout: network
lead: "See the mesh across Europe, and help it see more. Observers hear the mesh and report it, and every new one shows a bit more."
description: "How the MeshCore mesh in Europe becomes visible: observers report what they hear to the MeshCore Analyzer. Live numbers, and how to add your own observer."
---

The mesh itself keeps no record: a message goes from node to node and is
gone. What you see on [coverage maps](/map/) and in statistics comes from
observers. An observer is a node that also reports what it hears over MQTT,
through Wi-Fi or the internet. The report goes one way: nothing comes back onto
the mesh. A repeater (a node that passes messages on) with observer firmware keeps
repeating as before.

Observers across Europe report to the [MeshCore Analyzer](https://meshcore-analyzer.eu/)
at mqtt.meshcore-analyzer.eu. The Analyzer also reads other brokers, so an
observer there counts too. From those reports it builds the maps, the
statistics and the [channel list](/guides/channels/) on this site.

{{< callout type="tip" >}}
The mesh needs none of this. The observers' reports, the Analyzer, these maps
and tools go over the internet. In a power cut or when the internet is down, they stop. The
mesh keeps passing messages by radio, through every repeater that still has
power, such as the ones on solar. The tools are there to see and plan the
mesh, not to run it.
{{< /callout >}}
