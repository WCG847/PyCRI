# PYCRI: The high-level wrapper of CRIWare (2000s)

## About
PyCRI is an initiative to replicate the CRIWare logic on PS2. Using Python with low-level bindings, we strive for cycle-accurate SDK, although some elements may be stubbed, replaced with a suitable alternative, or optimised out.
<br>  <br>  Drawing inspiration from high-level wrappers for PlayStation (i.e) PS2SDK, we believe that such a concept is feasible in Python.

<br> Keeping in mind the limitations of Python, we developed this as a proof of concept/educational material. It is better to find an alternative for C for anything low-latency-like.

## Roadmap

| Goals | Subsystem | Category | Comments
| ----- | --------- | -------- | --------
| Initialisation | DVD, Host, Memory | Subsystem General | ✅
| Add Device | DVD, Host, Memory | Subsystem Device | ✅
| Register error handlers | DVD, Host, Memory | Subsystem Error Handling | ✅
| Add core logic | DVD, Host, Memory | Subsystem Logic | W.I.P.
<!-- EOT -->
## NOTICE
THIS PROJECT IS NOT ASSOCIATED WITH CRI Middleware Co., Ltd.®. THIS IS SOLELY AN INDEPENDENT RECREATION.
