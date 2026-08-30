unit Unit1;

{$mode objfpc}{$H+}

interface

uses
  Classes, SysUtils, Forms, Controls, Graphics, Dialogs, StdCtrls, ComCtrls,
  ExtCtrls, StrUtils;

type

  { TForm1 }

  TForm1 = class(TForm)
    Button1: TButton;
    Button2: TButton;
    BrokerIP: TEdit;
    BrokerPort: TEdit;
    Button3: TButton;
    Button4: TButton;
    Button5: TButton;
    DevIdent: TEdit;
    DevName: TEdit;
    DevManu: TEdit;
    DevModel: TEdit;
    Label5: TLabel;
    Label6: TLabel;
    Label7: TLabel;
    ListBox1: TListBox;
    LVar: TEdit;
    EntryName: TEdit;
    Panel1: TPanel;
    ScrPath: TEdit;
    TabSheet3: TTabSheet;
    UniqueID: TEdit;
    ExtPath: TEdit;
    Label1: TLabel;
    Label2: TLabel;
    Label3: TLabel;
    Label4: TLabel;
    OpenDialog1: TOpenDialog;
    PageControl1: TPageControl;
    SelectDirectoryDialog1: TSelectDirectoryDialog;
    TabSheet1: TTabSheet;
    TabSheet2: TTabSheet;
    procedure Button1Click(Sender: TObject);
    procedure Button2Click(Sender: TObject);
    procedure Button3Click(Sender: TObject);
    procedure Button4Click(Sender: TObject);
    procedure Button5Click(Sender: TObject);
  private

  public

  end;

var
  Form1: TForm1;

implementation

{$R *.lfm}

{ TForm1 }

procedure TForm1.Button2Click(Sender: TObject);
begin
     if SelectDirectoryDialog1.Execute then
         ExtPath.Text := SelectDirectoryDialog1.FileName;
end;

procedure TForm1.Button3Click(Sender: TObject);
begin
     if OpenDialog1.Execute then
        ScrPath.Text := OpenDialog1.FileName;

end;

procedure TForm1.Button1Click(Sender: TObject);
var
  Lines: TStringList;
  i, j: Integer;
begin
     if not FileExists(ScrPath.Text) then
  begin
    ShowMessage('Python file not found.');
    Exit;
  end;

  Lines := TStringList.Create;
  try
    Lines.LoadFromFile(ScrPath.Text);

    for i := 0 to Lines.Count - 1 do
        begin
          // ================================
          // SIMCONNECT PATH
          // ================================
          if Trim(Lines[i]) = '# CONFIG:SIMCONNECT_PATH' then
          begin
            for j := i + 1 to Lines.Count - 1 do
            begin
              if Pos('Ext_Path', Trim(Lines[j])) = 1 then
              begin
                Lines[j] := 'Ext_Path = r"' + ExtPath.Text + '"';
                Break;
              end;
            end;
          end;

          // ================================
          // MQTT BROKER
          // ================================
          if Trim(Lines[i]) = '# CONFIG:MQTT_BROKER' then
          begin
            for j := i + 1 to Lines.Count - 1 do
            begin
              if Pos('MQTT_BROKER', Trim(Lines[j])) = 1 then
              begin
                Lines[j] := 'MQTT_BROKER = "' + BrokerIP.Text + '"';
                Break;
              end;
            end;
          end;

    // ================================
      // MQTT PORT
      // ================================
      if Trim(Lines[i]) = '# CONFIG:MQTT_PORT' then
      begin
        for j := i + 1 to Lines.Count - 1 do
        begin
          if Pos('MQTT_PORT', Trim(Lines[j])) = 1 then
          begin
            Lines[j] := 'MQTT_PORT = "' + BrokerPort.Text + '"';
            Break;
          end;
        end;
      end;
    end;

    Lines.SaveToFile(ScrPath.Text);
    ShowMessage('Script updated successfully.');

  finally
    Lines.Free;
  end;
end;


procedure InsertAfterMarker(Lines: TStringList;
                            const Marker: String;
                            const NewLines: array of String);
var
  i, j: Integer;
begin
  for i := 0 to Lines.Count - 1 do
    if Trim(Lines[i]) = Marker then
    begin
      for j := High(NewLines) downto Low(NewLines) do
        Lines.Insert(i + 1, NewLines[j]);
      Exit;
    end;
end;

procedure TForm1.Button4Click(Sender: TObject);
var
  Lines: TStringList;
begin
  if not FileExists(ScrPath.Text) then
  begin
    ShowMessage('Script file not found.');
    Exit;
  end;

  Lines := TStringList.Create;
  try
    Lines.LoadFromFile(ScrPath.Text);

    InsertAfterMarker(Lines,
      '# NEW TOPIC DEFINITIONS AFTER THIS LINE',
      [
        '',
        UpperCase(UniqueID.Text) + '_STATE_TOPIC = (',
        '    "homeassistant/binary_sensor/' +
            LowerCase(UniqueID.Text) +
            '/state"',
        ')',
        '',
        UpperCase(UniqueID.Text) + '_CONFIG_TOPIC = (',
        '    "homeassistant/binary_sensor/' +
            LowerCase(UniqueID.Text) +
            '/config"',
        ')',
        ''
      ]);

    InsertAfterMarker(Lines,
      '# NEW DISCOVERY DEFINITIONS AFTER THIS LINE',
      [
  '',
  LowerCase(UniqueID.Text) + '_discovery = {',
  '    "name": "' + EntryName.Text + '",',
  '    "unique_id": "' + LowerCase(UniqueID.Text) + '",',
  '    "state_topic": ' + UpperCase(UniqueID.Text) + '_STATE_TOPIC,',
  '    "payload_on": "ON",',
  '    "payload_off": "OFF",',
  '    "device": {',
  '        "identifiers": ["' + DevIdent.Text + '"],',
  '        "name": "' + DevName.Text + '",',
  '        "manufacturer": "' + DevManu.Text + '",',
  '        "model": "' + DevModel.Text + '"',
  '    }',
  '}',
  ''
]);

    InsertAfterMarker(Lines,
  '# NEW DISCOVERY PROCEDURES AFTER THIS LINE',
[
  '',
  'mqtt_client.publish(',
  '    ' + UpperCase(UniqueID.Text) + '_CONFIG_TOPIC,',
  '    json.dumps(' + LowerCase(UniqueID.Text) + '_discovery),',
  '    retain=True',
  ')',
  ''
]);

        InsertAfterMarker(Lines,
  '# NEW LVARS AFTER THIS LINE',
[
  UpperCase(UniqueID.Text) + '_LVAR = "(' + LVar.Text + ')"',
  ''
]);

        InsertAfterMarker(Lines,
  '# NEW LASTSTATES AFTER THIS LINE',
[
  '    "' + LowerCase(UniqueID.Text) + '": None,'
]);
                InsertAfterMarker(Lines,
  '# NEW ENTRIES AFTER THIS LINE',
[
  '        ' + LowerCase(UniqueID.Text) + ' = int(float(vr.get(' + UpperCase(UniqueID.Text) + ')))',
  ''
]);

                InsertAfterMarker(Lines,
          '# NEW PROCEDURES AFTER THIS LINE',
        [
           '',
           '        if ' + LowerCase(UniqueID.Text) + ' != last_state["' + LowerCase(UniqueID.Text) + '"]:',
           '            mqtt_client.publish(',
           '                ' + UpperCase(UniqueID.Text) + '_STATE_TOPIC,',
           '                "ON" if ' + LowerCase(UniqueID.Text) + ' else "OFF",',
           '                retain=True',
           '            )',
           '',
           '            print(f"' + UpperCase(UniqueID.Text) + ': {' + LowerCase(UniqueID.Text) + '}")',
           '            last_state["' + LowerCase(UniqueID.Text) + '"] = ' + LowerCase(UniqueID.Text)
        ]);


    Lines.SaveToFile(ScrPath.Text);

    ShowMessage('Done.');

  finally
    Lines.Free;
  end;
end;

procedure TForm1.Button5Click(Sender: TObject);
var
  SL: TStringList;
  i: Integer;
  Line, VarName: String;
  InSection: Boolean;
  p: Integer;
begin
  ListBox1.Clear;

  if not FileExists(ScrPath.Text) then
  begin
    ShowMessage('Script file not found.');
    Exit;
  end;
  SL := TStringList.Create;
  try
    SL.LoadFromFile(ScrPath.Text);

    InSection := False;

    for i := 0 to SL.Count - 1 do
    begin
      Line := Trim(SL[i]);

      if Line = '# NEW ENTRIES AFTER THIS LINE' then
      begin
        InSection := True;
        Continue;
      end;

      if Line = '# END OF ENTRIES' then
        Break;

      if InSection then
      begin
        // Ignore empty lines
        if Line = '' then
          Continue;
      // Find '='
        p := Pos('=', Line);
        if p > 1 then
        begin
          VarName := Trim(Copy(Line, 1, p - 1));
          ListBox1.Items.Add(VarName);
        end;
      end;
    end;

  finally
    SL.Free;
  end;
end;


end.

