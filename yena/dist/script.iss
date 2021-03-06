; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

[Setup]
; NOTE: The value of AppId uniquely identifies this application.
; Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{37EDB4E3-C151-4375-8C36-E127CC7908E7}
AppName=Penguin_run
AppVersion=1.5
;AppVerName=Penguin_run 1.5
AppPublisher=KPU
AppPublisherURL=http://www.kpu.ac.kr/
AppSupportURL=http://www.kpu.ac.kr/
AppUpdatesURL=http://www.kpu.ac.kr/
DefaultDirName={pf}\Penguin_run
DefaultGroupName=Penguin_run
OutputDir=C:\Users\USER\Desktop
OutputBaseFilename=setup
Compression=lzma
SolidCompression=yes

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "C:\2dgp\yena\dist\Penguin_Run.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\2dgp\yena\dist\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs
; NOTE: Don't use "Flags: ignoreversion" on any shared system files

[Icons]
Name: "{group}\Penguin_run"; Filename: "{app}\Penguin_Run.exe"
Name: "{commondesktop}\Penguin_run"; Filename: "{app}\Penguin_Run.exe"; Tasks: desktopicon

[Run]
Filename: "{app}\Penguin_Run.exe"; Description: "{cm:LaunchProgram,Penguin_run}"; Flags: nowait postinstall skipifsilent

