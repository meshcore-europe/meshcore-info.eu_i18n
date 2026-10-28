---
title: "Coverage maps"
layout: map
lead: "See where the mesh reaches, where nodes are and how messages travel. Communities across Europe run these maps."
description: "Live MeshCore maps, coverage maps and packet analysers for Europe and individual countries."
---

A node appears on these maps when its owner publishes it, or when an
*observer* hears it: a node that forwards what it hears over MQTT. So no map
is complete. Analysers show the traffic their observers receive: packets,
routes and channel activity. Direct messages stay encrypted, so no analyser
shows what they say.

A node sits on a map where its owner put it, which can be wrong or out of
date. A flood message travels several paths at once. A route on a map is the path
of the copy that arrived first; the others are not recorded.

These maps need the internet; the mesh does not. [Why](/network/)

Running a repeater, a node that passes messages on? Set its position with `set lat` and `set lon`, and maps
can place it. The [repeater guide](/repeater-guide/#config) shows how.
