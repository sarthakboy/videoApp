def handler(event, context):
    html_content = """
    <html>
    <head>
        <style>
            #root {
                width: 100vw;
                height: 100vh;
            }
        </style>
    </head>
    <body>
        <div id="root"></div>
    </body>
    <script src="https://unpkg.com/@zegocloud/zego-uikit-prebuilt/zego-uikit-prebuilt.js"></script>
    <script>
        window.onload = function () {
            function getUrlParams(url) {
                let urlStr = url.split('?')[1];
                const urlSearchParams = new URLSearchParams(urlStr);
                const result = Object.fromEntries(urlSearchParams.entries());
                return result;
            }

            // JavaScript code for initializing the video conferencing UI.
            // ...

            // Generate a Token by calling a method.
            // @param 1: appID
            // @param 2: serverSecret
            // @param 3: Room ID
            // @param 4: User ID
            // @param 5: Username
            const roomID = getUrlParams(window.location.href)['roomID'] || (Math.floor(Math.random() * 10000) + "");
            const userID = Math.floor(Math.random() * 10000) + "";
            const userName = "{{ name }}";
            const appID = 383530149;
            const serverSecret = "59be6bbc6d05db21e22b182a428cdce3";
            const kitToken = ZegoUIKitPrebuilt.generateKitTokenForTest(appID, serverSecret, roomID, userID, userName);

            const zp = ZegoUIKitPrebuilt.create(kitToken);
            zp.joinRoom({
                container: document.querySelector("#root"),
                sharedLinks: [{
                    name: 'Personal link',
                    url: window.location.protocol + '//' + window.location.host + window.location.pathname + '?roomID=' + roomID,
                }],
                scenario: {
                    mode: ZegoUIKitPrebuilt.VideoConference,
                },
                turnOnMicrophoneWhenJoining: false,
                turnOnCameraWhenJoining: false,
                showMyCameraToggleButton: true,
                showMyMicrophoneToggleButton: true,
                showAudioVideoSettingsButton: true,
                showScreenSharingButton: true,
                showTextChat: true,
                showUserList: true,
                maxUsers: 50,
                layout: "Grid",
                showLayoutButton: true,
            });
        }
    </script>
    </html>
    """

    return {
        'statusCode': 200,
        'body': html_content,
        'headers': {
            'Content-Type': 'text/html',
        },
    }
