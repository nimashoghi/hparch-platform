https://docs.microsoft.com/en-us/powershell/scripting/install/installing-powershell-core-on-linux?view=powershell-6#raspbian

    # Install prerequisites
    sudo apt-get install libunwind8

    # Grab the latest tar.gz
    wget https://github.com/PowerShell/PowerShell/releases/download/v7.0.0-preview.1/powershell-7.0.0-preview.1-linux-arm32.tar.gz

    # Make folder to put powershell
    mkdir ~/powershell

    # Unpack the tar.gz file
    tar -xvf ./powershell-7.0.0-preview.1-linux-arm32.tar.gz -C ~/powershell

    # Start PowerShell
    ~/powershell/pwsh
