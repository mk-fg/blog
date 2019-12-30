# Script to redirect from long-obsolete URLs to current static-blog ones

redirects = {
	"2010/11/From-Baselayout-to-Systemd-setup-on-Exherbo": "2010/11/05/from-baselayout-to-systemd-setup-on-exherbo.html",
	"2010/11/Moar-free-time": "2010/11/12/moar-free-time.html",
	"2010/12/Commandline-pulseaudio-mixer-tool": "2010/12/25/commandline-pulseaudio-mixer-tool.html",
	"2010/12/Further-improvements-on-notification-daemon": "2010/12/09/further-improvements-for-notification-daemon.html",
	"2010/12/MooseFS-usage-experiences": "2010/12/07/moosefs-usage-experiences.html",
	"2010/12/oslistdir-and-oswalk-in-python-without-lists-by-the-grace-of-c-api-generator-and-recursion-custom-stack": "2010/12/15/oslistdir-and-oswalk-in-python-without-lists-by-the-grace-of-c-api-generator-and-recursion-custom-stack.html",
	"2010/12/Sane-playback-for-online-streaming-video-and-via-stream-dumping": "2010/12/29/sane-playback-for-online-streaming-video-via-stream-dumping.html",
	"2010/12/zcat-bzcat-lzcat-xzcat-Arrrgh-Autodetection-rocks": "2010/12/11/zcat-bzcat-lzcat-xzcat-arrrgh-autodetection-rocks.html",
	"2010/1/Wheee-Ive-got-a-blog-": "2010/01/30/wheee-ive-got-a-blog.html",
	"2010/2/libnotify-notification-daemon-shortcomings-and-my-solution": "2010/02/26/libnotify-notification-daemon-shortcomings-and-my-solution.html",
	"2010/2/Listening-to-music-over-the-net-with-authentication-and-cache": "2010/02/17/listening-to-music-over-the-net-with-authentication-and-cache.html",
	"2010/2/My-simple-ok-not-quite-backup-system": "2010/02/11/my-simple-ok-not-quite-backup-system.html",
	"2010/2/My-simple-ok-not-quite-backup-system-implementation-backed-up-side": "2010/02/13/my-simple-ok-not-quite-backup-system-implementation-backed-up-side.html",
	"2010/2/My-simple-ok-not-quite-backup-system-implementation-backup-host": "2010/02/14/my-simple-ok-not-quite-backup-system-implementation-backup-host.html",
	"2010/2/POSIX-capabilities-for-python": "2010/02/01/posix-capabilities-for-python.html",
	"2010/2/snmpd-pyagentx-or-re-discovery-of-sfnet": "2010/02/28/snmpd-pyagentx-or-re-discovery-of-sfnet.html",
	"2010/3/Single-instance-daemon-or-invisible-dock": "2010/03/10/single-instance-daemon-or-invisible-dock.html",
	"2010/4/Auto-away-for-pidgin": "2010/04/10/auto-away-for-pidgin.html",
	"2010/4/Availability-stats-and-history-log-with-relational-database-postgresql": "2010/04/10/availability-stats-and-history-log-with-relational-database-postgresql.html",
	"2010/4/Exherbo-paludis-fossil-syncer": "2010/04/25/exherbo-paludis-fossil-syncer.html",
	"2010/4/LUKS-dm-crypt-rootfs-without-password-via-smartcard": "2010/04/25/luks-dm-crypt-rootfs-without-password-via-smartcard.html",
	"2010/4/Thoughts-on-VCS-supporting-documentation-and-Fossil": "2010/04/17/thoughts-on-vcs-supporting-documentation-and-fossil.html",
	"2010/5/Music-collection-updates-feed-via-musicbrainz-and-lastfm": "2010/05/08/music-collection-updates-feed-via-musicbrainz-and-lastfm.html",
	"2010/6/Drop-in-ccrypt-replacement-for-bournal": "2010/06/13/drop-in-ccrypt-replacement-for-bournal.html",
	"2010/6/Getting-rid-of-dead-bittorrent-trackers-for-rtorrent-by-scrubbing-torrent-files": "2010/06/05/getting-rid-of-dead-bittorrent-trackers-for-rtorrent-by-scrubbing-torrent-files.html",
	"2010/6/No-IPSec-on-a-stick-for-me-": "2010/06/14/no-ipsec-on-a-stick-for-me.html",
	"2010/8/Home-brewed-NAS-gluster-with-sensible-replication": "2010/08/15/home-brewed-nas-gluster-with-sensible-replication.html",
	"2010/9/Distributed-fault-tolerant-fs-take-2-MooseFS": "2010/09/09/distributed-fault-tolerant-fs-take-2-moosefs.html",
	"2010/9/Info-feeds": "2010/09/12/info-feeds.html",
	"2011/10/dm-crypt-password-caching-between-dracut-and-systemd-systemd-password-agent": "2011/10/23/dm-crypt-password-caching-between-dracut-and-systemd-systemd-password-agent.html",
	"2011/11/Running-stuff-like-firefox-flash-and-skype-with-apparmor": "2011/11/12/running-stuff-like-firefox-flash-and-skype-with-apparmor.html",
	"2011/2/cgroups-initialization-libcgroup-and-my-ad-hoc-replacement-for-it": "2011/02/26/cgroups-initialization-libcgroup-and-my-ad-hoc-replacement-for-it.html",
	"2011/2/Dashboard-for-enabled-services-in-systemd": "2011/02/27/dashboard-for-enabled-services-in-systemd.html",
	"2011/3/Auto-updating-desktop-background-with-scaling-via-LQR-and-some-other-tricks": "2011/03/05/auto-updating-desktop-background-with-scaling-via-lqr-and-some-other-tricks.html",
	"2011/3/Parallel-port-LED-notification-for-extra-high-system-load": "2011/03/14/parallel-port-led-notification-for-extra-high-system-load.html",
	"2011/3/Selective-IPv6-AAAA-DNS-resolution": "2011/03/19/selective-ipv6-aaaa-dns-resolution.html",
	"2011/4/Key-Value-storage-with-historyversioning-on-top-of-scm": "2011/04/18/key-value-storage-with-historyversioning-on-top-of-scm.html",
	"2011/4/xdiskusage-like-visualization-for-any-remote-machine": "2011/04/19/xdiskusage-like-visualization-for-any-remote-machine.html",
	"2011/5/Backup-of-5-million-tiny-files-and-paths": "2011/05/08/backup-of-5-million-tiny-files-and-paths.html",
	"2011/5/Fossil-to-Git-export-and-mirroring": "2011/05/02/fossil-to-git-export-and-mirroring.html",
	"2011/6/Using-csync2-for-security-sensitive-paths": "2011/06/12/using-csync2-for-security-sensitive-paths.html",
	"2011/8/Notification-daemon-in-python": "2011/08/14/notification-daemon-in-python.html",
	"2011/9/Detailed-process-memory-accounting-including-shared-and-swapped-one": "2011/09/16/detailed-process-memory-accounting-including-shared-and-swapped-one.html",
	"2012/2/Late-adventures-with-time-series-data-collection-and-representation": "2012/02/28/late-adventures-with-time-series-data-collection-and-representation.html",
	"2012/2/On-github-as-well-now": "2012/02/03/on-github-as-well-now.html",
	"2012/2/Phasing-out-fossil-completely": "2012/02/07/phasing-out-fossil-completely.html",
	"2012/6/Proper-ish-way-to-start-long-running-systemd-service-on-udev-event-device-hotplug": "2012/06/16/proper-ish-way-to-start-long-running-systemd-service-on-udev-event-device-hotplug.html",
	"2012/8/A-new-toy-to-play-with-TI-Launchpad-with-MSP430-MCU": "2012/08/16/a-new-toy-to-play-with-ti-launchpad-with-msp430-mcu.html",
	"2012/8/Unhosted-remoteStorage-idea": "2012/08/09/unhosted-remotestorage-idea.html",
	"2012/9/Terms-of-Service-Didnt-Read": "2012/09/16/terms-of-service-didnt-read.html",
	"2013/1/Migrating-configuration-settings-to-E17-enlightenment-0170-from-older-E-versions": "2013/01/16/migrating-configuration-settings-to-e17-enlightenment-0170-from-older-e-versions.html",
	"2013/1/PyParsing-vs-Yapps": "2013/01/21/pyparsing-vs-yapps.html",
}

def application(env, start_response):
	url = env['REQUEST_URI'].strip('/')
	url_redirect = redirects.get(url)

	if not url_redirect:
		start_response('404 Not Found', [('Content-Type', 'text/html')])
		err = f'404: Requested URL was not found: {url}'
		return [f'<img alt="{err}" title="{err}" src="/misc/ie404.png">'.encode()]

	url_redirect = f'/{url_redirect}'
	start_response( '301 Moved Permanently',
		[('Location', url_redirect), ('Content-Type', 'text/plain')] )
	return [f'Redirecting to: {url_redirect}\n'.encode()]
