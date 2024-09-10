{
	description = "flake for pi_accontrol";

	inputs = {
		nixpkgs.url = "github:NixOS/nixpkgs";
	};

	outputs = { self, nixpkgs }: 
	let
		pkgs = import nixpkgs { system = "aarch64-darwin"; };
	in
	{
		devShells.aarch64-darwin.default = pkgs.mkShell {
			packages = [
				(pkgs.python3.withPackages (p: with p; [
					flask
				]))
			];
		};
	};
}
