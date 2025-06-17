{
  description = "devShell for Python projects";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixpkgs-unstable";
    flake-parts.url = "github:hercules-ci/flake-parts";
  };

  outputs = inputs @ {
    self,
    nixpkgs,
    flake-parts,
    ...
  }:
    flake-parts.lib.mkFlake {inherit inputs;} {
      systems = builtins.attrNames nixpkgs.legacyPackages;
      perSystem = {
        config,
        self',
        inputs',
        pkgs,
        system,
        ...
      }: let
        pkgs = nixpkgs.legacyPackages.${system};
        modest = pkgs.fetchzip {
          url = "https://www.modestchecker.net/Downloads/Modest-Toolset-v3.1.292-gd8c426d04-linux-x64.zip";
          hash = "sha256-pZZQuayrr0fUevxplgV0CXod/Fyt7yGL6U7jJ0Gyhy8=";
        };
      in {
        devShells.default = pkgs.mkShell {
          name = "python devShell";
          buildInputs = with pkgs; [
            python314
          ];
          shellHook = ''
            export MODEST_PATH="${modest}/modest"
          '';
        };
      };
    };
}
