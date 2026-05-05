# Sonoyuncu Client Freezer & GPU Limiter

After the Sonoyuncu Client was updated, I noticed that the Login Screen process continued running in the background, which decreased overall PC performance.

To fix this issue, I developed a Sonoyuncu Client Login Screen Freezer / GPU Limiter.

When you AFK on 50 accounts, the client starts 50 "UISubProcess.exe" processes.  
The UISubProcessFreeze script freezes these processes, reducing their GPU usage to 0%.

This significantly increases PC performance and may reduce FPS drops.

⚠ CPU Limiter (Experimental)

The CPU limiter still needs improvement. Currently, it freezes all Sonoyuncu Clients, but it has a critical issue:
When you run the file, all clients freeze and eventually disconnect from the server.

For example, if the server is under maintenance and you want to play another game (such as League of Legends) while running 50 clients, the CPU limiter may improve performance — but it may also cause disconnections.
Discord :
oxygenqqw
987018545185570857
