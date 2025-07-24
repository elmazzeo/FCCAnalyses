'''
Ntuple production for FCC-hh analysis of ttH(yy)
'''
from argparse import ArgumentParser
import os


# Mandatory: Analysis class where the user defines the operations on the
# dataframe.
class Analysis():
    '''
    FCC-hh ttH(yy) analysis
    '''
    def __init__(self, cmdline_args):
        parser = ArgumentParser(
            description='Additional analysis arguments',
            usage='Provide additional arguments after analysis script path')
        parser.add_argument('--photon-pt', default='10.', type=float,
                             help='Minimal pT of the selected photons.')
        parser.add_argument('--jet-pt', default='25.', type=float,
                             help='Minimal pT of the selected jets.')
        parser.add_argument('--detailed', action='store_true',
                             help='Dump detailed ntuples.', default=False)
        parser.add_argument('--ttH', action='store_true',
                                help='Dump ttH-specific variables', default=False)
        parser.add_argument('--ttZ', action='store_true',  
                                help='Dump ttZ-specific variables', default=False)
        # Parse additional arguments not known to the FCCAnalyses parsers
        # All command line arguments know to fccanalysis are provided in the
        # `cmdline_arg` dictionary.
        self.ana_args, _ = parser.parse_known_args(cmdline_args['unknown'])

        # Mandatory: List of processes to run over
        self.process_list = {
            # # Add your processes like this: 
            ## '<name of process>':{'fraction':<fraction of events to run over>, 'chunks':<number of chunks to split the output into>, 'output':<name of the output file> }, 
            # # - <name of process> needs to correspond either the name of the input .root file, or the name of a directory containing root files 
            # # If you want to process only part of the events, split the output into chunks or give a different name to the output use the optional arguments
            # # or leave blank to use defaults = run the full statistics in one output file named the same as the process:
            # ttH(yy) signal
            #'mgp8_pp_tth01j_5f_84TeV_haaexcl' : {'chunks': 100}, # ttH->yy at 84 TeV
            #'mgp8_pp_tth01j_5f_haa' : {'chunks': 100}, # ttH->yy at 100 TeV
            # Backgrounds 
            #'mgp8_pp_ttaa01j_5f_84TeV': {'chunks':100}, #ttyy+jets at 84 TeV
            #'mgp8_pp_ttaa_semilep_5f_100TeV': {'chunks':5}, #ttyy semilep at 100 TeV 
            #'mgp8_pp_Vaajj_HF_5f_84TeV' : {'chunks': 100}, #V+yy+bb/cc at 84 TeV
            # HH->bbyy test
            #'pwp8_pp_hh_lambda100_5f_hhbbaa' : {'chunks': 100},
            # ttZ(ee) signal
            #"mgp8_pp_ttz01j_5f_84TeV_zee" : {'chunks': 100}, # ttZ->ee at 84 TeV
            # Backgrounds
            #"mgp8_pp_WZjj_HF_5f_84TeV_zeewlep" : {'chunks': 100}, # W(->lep)Z(->ee)+jets at 84 TeV
            #"mgp8_pp_ZZjj_HF_5f_84TeV_zzlep" : {'chunks': 100}, # Z(->lep)Z(->ee)+jets at 84 TeV
            #"mgp8_pp_tZj_5f_84TeV_zeewlep" : {'chunks': 100}, # t(->lep)Z(->ee)+jets at 84 TeV
            #"mgp8_pp_tWZj_5f_84TeV_zee" : {'chunks': 100}, # tWZ(->ee)+jets at 84 TeV
            # Q-binned pT ttH(yy) signal
            "mgp8_pp_tth_5f_Q_0_1000_84TeV_haaexcl" : {'chunks': 100}, # ttH->yy at 84 TeV, Q-binned
            "mgp8_pp_tth_5f_Q_1000_3000_84TeV_haaexcl" : {'chunks': 100}, # ttH->yy at 84 TeV, Q-binned
            "mgp8_pp_tth_5f_Q_3000_10000_84TeV_haaexcl" : {'chunks': 100}, # ttH->yy at 84 TeV, Q-binned
            "mgp8_pp_tth_5f_Q_10000_84000_84TeV_haaexcl" : {'chunks': 100}, # ttH->yy at 84 TeV, Q-binned
            # Q-binned ttyy background
            "mgp8_pp_ttaa_Q_0_500_5f_84TeV" : {'chunks': 100}, # ttyy at 84 TeV, Q-binned
            "mgp8_pp_ttaa_Q_500_1000_5f_84TeV" : {'chunks': 100}, # ttyy at 84 TeV, Q-binned
            "mgp8_pp_ttaa_Q_1000_2000_5f_84TeV" : {'chunks': 100}, # ttyy at 84 TeV, Q-binned
            "mgp8_pp_ttaa_Q_2000_5000_5f_84TeV" : {'chunks': 100}, # ttyy at 84 TeV, Q-binned
            "mgp8_pp_ttaa_Q_5000_84000_5f_84TeV" : {'chunks': 100}, # ttyy at 84 TeV, Q-binned
            # Q-binned V+yy+bb/cc background
            "mgp8_pp_vaa_Q_0_500_5f_84TeV": {'chunks': 100}, # V+yy+bb/cc at 84 TeV, Q-binned
            "mgp8_pp_vaa_Q_500_1000_5f_84TeV": {'chunks': 100}, # V+yy+bb/cc at 84 TeV, Q-binned
            "mgp8_pp_vaa_Q_1000_2000_5f_84TeV": {'chunks': 100}, # V+yy+bb/cc at 84 TeV, Q-binned
            "mgp8_pp_vaa_Q_2000_5000_5f_84TeV": {'chunks': 100}, # V+yy+bb/cc at 84 TeV, Q-binned
            "mgp8_pp_vaa_Q_5000_84000_5f_84TeV": {'chunks': 100}, # V+yy+bb/cc at 84 TeV, Q-binned
        }

        # Mandatory: Input directory where to find the samples, or a production tag when running over the centrally produced
        # samples (this points to the yaml files for getting sample statistics)
        self.input_dir = '/eos/experiment/fcc/hh/generation/DelphesEvents/fcc_v07/II/'
        #self.input_dir =  '/eos/user/b/bistapf/FCChh_sample_testers/'

        # Optional: output directory, default is local running directory
        self.output_dir = '/eos/user/e/elmazzeo/ttH@FCC-hh/results/2025-07-09' + '/ntuples/'

        # Optional: analysisName, default is ''
        self.analysis_name = 'FCC-hh ttH(yy) analysis'

        # Optional: number of threads to run on, default is 'all available'
        # self.n_threads = 4

        # Optional: running on HTCondor, default is False
        self.run_batch = True

        # Optional: Use weighted events
        self.do_weighted = True 

        # Optional: read the input files with podio::DataSource 
        self.use_data_source = False # explicitly use old way in this version 

        # Optional: test file that is used if you run with the --test argument 
        self.test_file = 'root://eospublic.cern.ch//eos/experiment/fcc/hh/' \
                         'generation/DelphesEvents/fcc_v07/II/mgp8_pp_tth_5f_Q_0_1000_84TeV_haaexcl/' \
                         'events_000189647.root'

    # Mandatory: analyzers function to define the analysis graph, please make
    # sure you return the dataframe, in this example it is dframe2
    def analyzers(self, dframe):
        '''
        Analysis graph.
        '''

        dframe2 = (
            dframe

            ########################################### DEFINITION OF VARIABLES ########################################### 

            # generator event weight
            .Define("weight",  "EventHeader.weight")
            # event number
            .Define("event_number", "EventHeader.eventNumber")
            .Define("run_number", "EventHeader.runNumber")
            ################################## RECO TO TRUTH ASSOCIATIONS ##################################
            # reco-to-MC particle association
            .Alias("MCRecoAssociations0", "_MCRecoAssociations_from.index")
            .Alias("MCRecoAssociations1", "_MCRecoAssociations_to.index")
            .Define("RP2MC_index", "FCCAnalyses::ReconstructedParticle2MC::getRP2MC_index(MCRecoAssociations0, MCRecoAssociations1, ReconstructedParticles)")
            ########################################### PHOTONS ########################################### 
            # all photons passing particle ID
            .Define("gamma_original",  "FCCAnalyses::ReconstructedParticle::get(Photon_objIdx.index, ReconstructedParticles)")
            .Define("photon_indices", "FCCAnalyses::ReconstructedParticle::get_idx_clean(Photon_objIdx.index)")
            .Define("gamma", "FCCAnalyses::SmearObjects::SmearedReconstructedParticle(1, 22, 2, event_number[0], false)(ReconstructedParticles, RP2MC_index, Particle, photon_indices)")
            .Define("idx_gamma",  "FCCAnalyses::ReconstructedParticle::get_idx(gamma)") # get indices of each photon in the "gamma" collection
            .Define("idx_gamma1", "photon_indices")
            # apply pT selection
            .Define("selpt_gamma", "FCCAnalyses::ReconstructedParticle::sel_pt({photon_pt})(gamma)".format(photon_pt=self.ana_args.photon_pt))
            # for each selection, keep track of the indices of the selected particles in the original collections
            .Define("idx_selpt_gamma", "FCCAnalyses::ReconstructedParticle::sel_pt({photon_pt})(gamma, idx_gamma)".format(photon_pt=self.ana_args.photon_pt))
            .Define("idx_selpt_gamma1", "FCCAnalyses::ReconstructedParticle::sel_pt({photon_pt})(gamma, idx_gamma1)".format(photon_pt=self.ana_args.photon_pt))
            # apply |eta| selection
            .Define("sel_gamma_unsort", "FCCAnalyses::ReconstructedParticle::sel_eta(6.)(selpt_gamma)")
            .Define("idx_sel_gamma_unsort", "FCCAnalyses::ReconstructedParticle::sel_eta(6.)(selpt_gamma, idx_selpt_gamma)")
            .Define("idx_sel_gamma_unsort1", "FCCAnalyses::ReconstructedParticle::sel_eta(6.)(selpt_gamma, idx_selpt_gamma1)")
            # sort photons by pT
            .Define("sel_gamma", "AnalysisFCChh::SortParticleCollection(sel_gamma_unsort)") 
            .Define("idx_sel_gamma", "AnalysisFCChh::SortParticleCollection(sel_gamma_unsort, idx_sel_gamma_unsort)")
            .Define("idx_sel_gamma1", "AnalysisFCChh::SortParticleCollection(sel_gamma_unsort, idx_sel_gamma_unsort1)")
            # output branches
            .Define("n_photons",  "FCCAnalyses::ReconstructedParticle::get_n(sel_gamma)") 
            .Define("E_photons",  "FCCAnalyses::ReconstructedParticle::get_e(sel_gamma)")
            .Define("pT_photons",  "FCCAnalyses::ReconstructedParticle::get_pt(sel_gamma)")
            .Define("eta_photons",  "FCCAnalyses::ReconstructedParticle::get_eta(sel_gamma)")
            .Define("phi_photons",  "FCCAnalyses::ReconstructedParticle::get_phi(sel_gamma)")
            # H(yy) if it exists, if there are no 2 selected photons, doesnt get filled 
            .Define("yy_pairs_unmerged", "AnalysisFCChh::getPairs(sel_gamma)") # retrieves the leading pT pair of all possible 
            .Define("yy_pairs", "AnalysisFCChh::merge_pairs(yy_pairs_unmerged)") # merge pair into one object to access inv masses etc
            .Define("m_yy", "FCCAnalyses::ReconstructedParticle::get_mass(yy_pairs)")
            .Define("pT_yy", "FCCAnalyses::ReconstructedParticle::get_pt(yy_pairs)")
            .Define("rapidity_yy", "FCCAnalyses::ReconstructedParticle::get_y(yy_pairs)")
            # theta between the two photons
            .Define("theta_y_y", "(n_photons > 1) ? FCCAnalyses::ReconstructedParticle::get_tlv(sel_gamma[0]).Vect().Angle(FCCAnalyses::ReconstructedParticle::get_tlv(sel_gamma[1]).Vect()) : -999.")
            .Define("cos_theta_y_y", "(n_photons > 1) ? TMath::Cos(theta_y_y) : -999.")
            # leading photon
            .Define("E_y1", "(n_photons > 0) ? E_photons[0] : -999.")
            .Define("pT_y1", "(n_photons > 0) ? pT_photons[0] : -999.")
            .Define("eta_y1", "(n_photons > 0) ? eta_photons[0] : -999.")
            .Define("phi_y1", "(n_photons > 0) ? phi_photons[0] : -999.")
            .Define("rel_pT_y1", "(n_photons > 0) ? pT_y1/m_yy[0] : -999.")
            .Define("idx_y1", "(n_photons > 0) ? idx_sel_gamma1[0] : -999.")
            # subleading photon
            .Define("E_y2", "(n_photons > 1) ? E_photons[1] : -999.")
            .Define("pT_y2", "(n_photons > 1) ? pT_photons[1] : -999.")
            .Define("eta_y2", "(n_photons > 1) ? eta_photons[1] : -999.")
            .Define("phi_y2", "(n_photons > 1) ? phi_photons[1] : -999.")
            .Define("rel_pT_y2", "(n_photons > 1) ? pT_y2/m_yy[0] : -999.")
            .Define("idx_y2", "(n_photons > 1) ? idx_sel_gamma1[1] : -999.")
            .Define("DR_y_y", "(n_photons > 1) ? FCCAnalyses::ReconstructedParticle::get_tlv(sel_gamma[0]).DeltaR(FCCAnalyses::ReconstructedParticle::get_tlv(sel_gamma[1])) : -999.")
            # reco-to-MC particle association
            .Define("true_TLV", "ReconstructedParticle2MC::getRP2MC_tlv(MCRecoAssociations0, MCRecoAssociations1, ReconstructedParticles, Particle)")
            .Define("pdgID_y1", "(idx_y1 >= 0 ) ? ReconstructedParticles.PDG.at(idx_y1) : -999")
            .Define("pdgID_y2", "(idx_y2 >= 0 ) ? ReconstructedParticles.PDG.at(idx_y2) : -999")
            .Define("true_TLV_y1", "(idx_y1 >= 0) ? true_TLV[idx_y1] : TLorentzVector(0.,0.,0.,0.)")
            .Define("true_TLV_y2", "(idx_y2 >= 0) ? true_TLV[idx_y2] : TLorentzVector(0.,0.,0.,0.)")
            .Define('true_E_y1',"(idx_y1 >= 0) ? true_TLV_y1.E() : -999.")
            .Define('true_pT_y1',"(idx_y1 >= 0) ? true_TLV_y1.Pt() : -999.")
            .Define('true_eta_y1',"(idx_y1 >= 0) ? true_TLV_y1.Eta() : -999.")
            .Define('true_phi_y1',"(idx_y1 >= 0) ? true_TLV_y1.Phi() : -999.")
            .Define('true_E_y2',"(idx_y2 >= 0) ? true_TLV_y2.E() : -999.")
            .Define('true_pT_y2',"(idx_y2 >= 0) ? true_TLV_y2.Pt() : -999.")
            .Define('true_eta_y2',"(idx_y2 >= 0) ? true_TLV_y2.Eta() : -999.")
            .Define('true_phi_y2',"(idx_y2 >= 0) ? true_TLV_y2.Phi() : -999.")
            .Define('true_m_yy',"(idx_y1 >= 0 && idx_y2 >=0) ? (true_TLV_y1 + true_TLV_y2).M() : -999.")
            .Define('true_DR_y_y',"(idx_y1 >= 0 && idx_y2 >=0) ? true_TLV_y1.DeltaR(true_TLV_y2) : -999.")
            .Define('true_pT_yy',"(idx_y1 >= 0 && idx_y2 >=0) ? (true_TLV_y1 + true_TLV_y2).Pt() : -999.")
            .Define("true_theta_y_y", "(idx_y1 >= 0 && idx_y2 >=0) ? true_TLV_y1.Vect().Angle(true_TLV_y2.Vect()) : -999.")
            .Define("true_cos_theta_y_y", "(idx_y1 >= 0 && idx_y2 >=0) ? TMath::Cos(true_theta_y_y) : -999.")
            # check if the selected reco photons have Higgs parents
            .Define("has_higgs_parent_y1", "(idx_y1 >= 0) ? AnalysisFCChh::hasHiggsParent(Particle.at(RP2MC_index[idx_y1]), _Particle_parents, Particle) : false")
            .Define("has_higgs_parent_y2", "(idx_y2 >= 0) ? AnalysisFCChh::hasHiggsParent(Particle.at(RP2MC_index[idx_y2]), _Particle_parents, Particle) : false")       
            # get truth photons from Higgs
            .Define("HtoYY_truth_photons", "AnalysisFCChh::getPhotonsFromH(Particle, _Particle_parents)")
            .Define("HtoYY_truth_photons_TLV", "FCCAnalyses::MCParticle::get_tlv(HtoYY_truth_photons)")
            .Define("HtoYY_n_truth_photons", "FCCAnalyses::MCParticle::get_n(HtoYY_truth_photons)")
            .Define("HtoYY_E_truth_photons", "FCCAnalyses::MCParticle::get_e(HtoYY_truth_photons)")
            .Define("HtoYY_pT_truth_photons", "FCCAnalyses::MCParticle::get_pt(HtoYY_truth_photons)")
            .Define("HtoYY_eta_truth_photons", "FCCAnalyses::MCParticle::get_eta(HtoYY_truth_photons)")
            .Define("HtoYY_phi_truth_photons", "FCCAnalyses::MCParticle::get_phi(HtoYY_truth_photons)")
            .Define("HtoYY_truth_E_y1", "(HtoYY_n_truth_photons > 0) ? HtoYY_E_truth_photons[0] : -999.")
            .Define("HtoYY_truth_pT_y1", "(HtoYY_n_truth_photons > 0) ? HtoYY_pT_truth_photons[0] : -999.")
            .Define("HtoYY_truth_eta_y1", "(HtoYY_n_truth_photons > 0) ? HtoYY_eta_truth_photons[0] : -999.")
            .Define("HtoYY_truth_phi_y1", "(HtoYY_n_truth_photons > 0) ? HtoYY_phi_truth_photons[0] : -999.")
            .Define("HtoYY_truth_E_y2", "(HtoYY_n_truth_photons > 1) ? HtoYY_E_truth_photons[1] : -999.")
            .Define("HtoYY_truth_pT_y2", "(HtoYY_n_truth_photons > 1) ? HtoYY_pT_truth_photons[1] : -999.")
            .Define("HtoYY_truth_eta_y2", "(HtoYY_n_truth_photons > 1) ? HtoYY_eta_truth_photons[1] : -999.")
            .Define("HtoYY_truth_phi_y2", "(HtoYY_n_truth_photons > 1) ? HtoYY_phi_truth_photons[1] : -999.")
            .Define("HtoYY_truth_m_yy", "(HtoYY_n_truth_photons > 1) ? (HtoYY_truth_photons_TLV[0] + HtoYY_truth_photons_TLV[1]).M() : -999.")  
            # TLV test for myy resolution
            .Define("TLV_y1", "(n_photons > 0) ? AnalysisFCChh::getTLV(E_y1/TMath::CosH(true_eta_y1), true_eta_y1, true_phi_y1, E_y1) : TLorentzVector(0.,0.,0.,0.)")
            .Define("TLV_y2", "(n_photons > 1) ? AnalysisFCChh::getTLV(E_y2/TMath::CosH(true_eta_y2), true_eta_y2, true_phi_y2, E_y2) : TLorentzVector(0.,0.,0.,0.)")
            .Define("test_m_yy", "(n_photons > 1) ? (TLV_y1 + TLV_y2).M() : -999.")
            .Define("test_pT_yy", "(n_photons > 1) ? (TLV_y1 + TLV_y2).Pt() : -999.")
            .Define("test_theta_y_y", "(n_photons > 1) ? TLV_y1.Vect().Angle(TLV_y2.Vect()) : -999.")
            .Define("test_cos_theta_y_y", "(n_photons > 1) ? TMath::Cos(test_theta_y_y) : -999.")
            ########################################### ELECTRONS ########################################### 
            .Define("electrons",  "FCCAnalyses::ReconstructedParticle::get(Electron_objIdx.index, ReconstructedParticles)")
            .Define("sel_electrons_unsort", "FCCAnalyses::ReconstructedParticle::sel_pt(15.)(electrons)")
            .Define("idx_electrons_unsort", "FCCAnalyses::ReconstructedParticle::sel_pt(15.)(electrons, Electron_objIdx.index)")
            # sort electrons by |mee - mZ| for the first pair, and then the rest by pT
            .Define("sel_electrons", "AnalysisFCChh::SortLeptonsFromZDecay(sel_electrons_unsort, idx_electrons_unsort, Particle, idx_electrons_unsort, RP2MC_index)")
            .Define("idx_electrons", "AnalysisFCChh::SortLeptonsIdxFromZDecay(sel_electrons_unsort, idx_electrons_unsort, Particle, idx_electrons_unsort, RP2MC_index)")
            # output branches
            .Define("n_electrons",  "FCCAnalyses::ReconstructedParticle::get_n(sel_electrons)")
            .Define("E_electrons",  "FCCAnalyses::ReconstructedParticle::get_e(sel_electrons)")
            .Define("pT_electrons",  "FCCAnalyses::ReconstructedParticle::get_pt(sel_electrons)")
            .Define("eta_electrons",  "FCCAnalyses::ReconstructedParticle::get_eta(sel_electrons)")
            .Define("phi_electrons",  "FCCAnalyses::ReconstructedParticle::get_phi(sel_electrons)")
            .Define("charge_electrons",  "FCCAnalyses::ReconstructedParticle::get_charge(sel_electrons)")
            # first two electrons
            # leading electron
            .Define("E_e1", "(n_electrons > 0) ? E_electrons[0] : -999.")
            .Define("pT_e1", "(n_electrons > 0) ? pT_electrons[0] : -999.")
            .Define("eta_e1", "(n_electrons > 0) ? eta_electrons[0] : -999.")
            .Define("phi_e1", "(n_electrons > 0) ? phi_electrons[0] : -999.")
            .Define("charge_e1", "(n_electrons > 0) ? charge_electrons[0] : -999.")
            .Define("idx_e1", "(n_electrons > 0) ? idx_electrons[0] : -999.")
            # subleading electron
            .Define("E_e2", "(n_electrons > 1) ? E_electrons[1] : -999.")
            .Define("pT_e2", "(n_electrons > 1) ? pT_electrons[1] : -999.")
            .Define("eta_e2", "(n_electrons > 1) ? eta_electrons[1] : -999.")
            .Define("phi_e2", "(n_electrons > 1) ? phi_electrons[1] : -999.")
            .Define("charge_e2", "(n_electrons > 1) ? charge_electrons[1] : -999.")
            .Define("idx_e2", "(n_electrons > 1) ? idx_electrons[1] : -999.")
            # ee object from e1 and e2
            .Define("ee_best_unmerged", "(n_electrons > 1) ? AnalysisFCChh::getPair(sel_electrons.at(0), sel_electrons.at(1)) : ROOT::VecOps::RVec<AnalysisFCChh::RecoParticlePair>(0)") # retrieves the ee object from the first two electrons
            .Define("ee_best", "AnalysisFCChh::merge_pairs(ee_best_unmerged)") # merge pair into one object to access inv masses etc
            .Define("m_ee", "FCCAnalyses::ReconstructedParticle::get_mass(ee_best)")
            .Define("pT_ee", "FCCAnalyses::ReconstructedParticle::get_pt(ee_best)")
            .Define("DR_e_e", "(n_electrons > 1) ? FCCAnalyses::ReconstructedParticle::get_tlv(sel_electrons.at(0)).DeltaR(FCCAnalyses::ReconstructedParticle::get_tlv(sel_electrons.at(1))) : -999.")

            # third electron
            .Define("E_e3", "(n_electrons > 2) ? E_electrons[2] : -999.")
            .Define("pT_e3", "(n_electrons > 2) ? pT_electrons[2] : -999.")
            .Define("eta_e3", "(n_electrons > 2) ? eta_electrons[2] : -999.")
            .Define("phi_e3", "(n_electrons > 2) ? phi_electrons[2] : -999.")
            .Define("charge_e3", "(n_electrons > 2) ? charge_electrons[2] : -999.")
            .Define("idx_e3", "(n_electrons > 2) ? idx_electrons[2] : -999.")
            # fourth electron
            .Define("E_e4", "(n_electrons > 3) ? E_electrons[3] : -999.")
            .Define("pT_e4", "(n_electrons > 3) ? pT_electrons[3] : -999.")
            .Define("eta_e4", "(n_electrons > 3) ? eta_electrons[3] : -999.")
            .Define("phi_e4", "(n_electrons > 3) ? phi_electrons[3] : -999.")
            .Define("charge_e4", "(n_electrons > 3) ? charge_electrons[3] : -999.")
            .Define("idx_e4", "(n_electrons > 3) ? idx_electrons[3] : -999.")
            # ee object from e3 and e4
            .Define("ee_second_unmerged", "AnalysisFCChh::getPair(sel_electrons.at(2), sel_electrons.at(3))") # retrieves the ee object from the first two electrons
            .Define("ee_second", "AnalysisFCChh::merge_pairs(ee_second_unmerged)") # merge pair into one object to access inv masses etc
            .Define("m_ee_sublead", "FCCAnalyses::ReconstructedParticle::get_mass(ee_second)")
            .Define("pT_ee_sublead", "FCCAnalyses::ReconstructedParticle::get_pt(ee_second)")
            # Reco-to-MC particle association for the two leading electrons
            .Define("true_TLV_e1", "(idx_e1 >= 0) ? true_TLV[idx_e1] : TLorentzVector(0.,0.,0.,0.)")
            .Define("true_TLV_e2", "(idx_e2 >= 0) ? true_TLV[idx_e2] : TLorentzVector(0.,0.,0.,0.)")
            .Define("true_E_e1", "(idx_e1 >= 0) ? true_TLV_e1.E() : -999.")
            .Define("true_pT_e1", "(idx_e1 >= 0) ? true_TLV_e1.Pt() : -999.")
            .Define("true_eta_e1", "(idx_e1 >= 0) ? true_TLV_e1.Eta() : -999.")
            .Define("true_phi_e1", "(idx_e1 >= 0) ? true_TLV_e1.Phi() : -999.")
            .Define("true_charge_e1", "(idx_e1 >= 0) ? FCCAnalyses::MCParticle::get_charge(Particle.at(RP2MC_index[idx_e1])) : -999")
            .Define("true_E_e2", "(idx_e2 >= 0) ? true_TLV_e2.E() : -999.")
            .Define("true_pT_e2", "(idx_e2 >= 0) ? true_TLV_e2.Pt() : -999.")
            .Define("true_eta_e2", "(idx_e2 >= 0) ? true_TLV_e2.Eta() : -999.")
            .Define("true_phi_e2", "(idx_e2 >= 0) ? true_TLV_e2.Phi() : -999.")
            .Define("true_charge_e2", "(idx_e2 >= 0) ? FCCAnalyses::MCParticle::get_charge(Particle.at(RP2MC_index[idx_e2])) : -999")
            .Define("true_m_ee", "(idx_e1 >= 0 && idx_e2 >=0) ? (true_TLV_e1 + true_TLV_e2).M() : -999.")
            .Define("true_DR_e_e", "(idx_e1 >= 0 && idx_e2 >=0) ? true_TLV_e1.DeltaR(true_TLV_e2) : -999.")
            .Define("true_pT_ee", "(idx_e1 >= 0 && idx_e2 >=0) ? (true_TLV_e1 + true_TLV_e2).Pt() : -999.")
            ########################################### MUONS ########################################### 
            .Define("muons",  "FCCAnalyses::ReconstructedParticle::get(Muon_objIdx.index, ReconstructedParticles)")
            .Define("sel_muons_unsort", "FCCAnalyses::ReconstructedParticle::sel_pt(15.)(muons)")
            .Define("idx_muons_unsort", "FCCAnalyses::ReconstructedParticle::sel_pt(15.)(muons, Muon_objIdx.index)")
            # sort muons by pT
            .Define("sel_muons", "AnalysisFCChh::SortParticleCollection(sel_muons_unsort)")
            .Define("idx_muons", "AnalysisFCChh::SortParticleCollection(sel_muons_unsort, idx_muons_unsort)")
            # output branches
            .Define("n_muons",  "FCCAnalyses::ReconstructedParticle::get_n(sel_muons)")
            .Define("E_muons",  "FCCAnalyses::ReconstructedParticle::get_e(sel_muons)")
            .Define("pT_muons",  "FCCAnalyses::ReconstructedParticle::get_pt(sel_muons)")
            .Define("eta_muons",  "FCCAnalyses::ReconstructedParticle::get_eta(sel_muons)")
            .Define("phi_muons",  "FCCAnalyses::ReconstructedParticle::get_phi(sel_muons)")
            .Define("charge_muons",  "FCCAnalyses::ReconstructedParticle::get_charge(sel_muons)")
            # ee object
            .Define("mumu_pairs_unmerged", "AnalysisFCChh::getPairs(sel_muons)") # retrieves the leading pT pair of all possible 
            .Define("mumu_pairs", "AnalysisFCChh::merge_pairs(mumu_pairs_unmerged)") # merge pair into one object to access inv masses etc
            .Define("m_mumu", "FCCAnalyses::ReconstructedParticle::get_mass(mumu_pairs)")
            .Define("pT_mumu", "FCCAnalyses::ReconstructedParticle::get_pt(mumu_pairs)")
            # first two muons (no truth matching)
            # leading muon
            .Define("E_mu1", "(n_muons > 0) ? E_muons[0] : -999.")
            .Define("pT_mu1", "(n_muons > 0) ? pT_muons[0] : -999.")
            .Define("eta_mu1", "(n_muons > 0) ? eta_muons[0] : -999.")
            .Define("phi_mu1", "(n_muons > 0) ? phi_muons[0] : -999.")
            .Define("charge_mu1", "(n_muons > 0) ? charge_muons[0] : -999.")
            .Define("idx_mu1", "(n_muons > 0) ? idx_muons[0] : -999.")
            # subleading muon
            .Define("E_mu2", "(n_muons > 1) ? E_muons[1] : -999.")
            .Define("pT_mu2", "(n_muons > 1) ? pT_muons[1] : -999.")
            .Define("eta_mu2", "(n_muons > 1) ? eta_muons[1] : -999.")
            .Define("phi_mu2", "(n_muons > 1) ? phi_muons[1] : -999.")
            .Define("charge_mu2", "(n_muons > 1) ? charge_muons[1] : -999.")
            .Define("idx_mu2", "(n_muons > 1) ? idx_muons[1] : -999.")
            ########################################### LEPTONS ########################################### 
            .Define("idx_leptons_all",  "AnalysisFCChh::concatenate(Muon_objIdx.index, Electron_objIdx.index)")
            .Define("leptons", "FCCAnalyses::ReconstructedParticle::get(idx_leptons_all, ReconstructedParticles)") 
            # select leptons with pT > 15 GeV
            .Define("sel_leptons_unsort", "FCCAnalyses::ReconstructedParticle::sel_pt(15.)(leptons)")
            .Define("idx_leptons_unsort", "FCCAnalyses::ReconstructedParticle::sel_pt(15.)(leptons, idx_leptons_all)")
            # sort leptons by |mll - mZ| for the first pair, and then the rest by pT
            .Define("sel_leptons", "AnalysisFCChh::SortLeptonsFromZDecay(sel_leptons_unsort, idx_leptons_unsort, Particle, idx_leptons_unsort, RP2MC_index)")
            .Define("idx_leptons", "AnalysisFCChh::SortLeptonsIdxFromZDecay(sel_leptons_unsort, idx_leptons_unsort, Particle, idx_leptons_unsort, RP2MC_index)")
            # get tLorentz vectors of the leptons
            .Define("lepton_tlv", "FCCAnalyses::ReconstructedParticle::get_tlv(sel_leptons)")
            # output branches
            .Define("n_leptons",  "FCCAnalyses::ReconstructedParticle::get_n(sel_leptons)")
            .Define("E_leptons",  "FCCAnalyses::ReconstructedParticle::get_e(sel_leptons)")
            .Define("pT_leptons",  "FCCAnalyses::ReconstructedParticle::get_pt(sel_leptons)")
            .Define("eta_leptons",  "FCCAnalyses::ReconstructedParticle::get_eta(sel_leptons)")
            .Define("phi_leptons",  "FCCAnalyses::ReconstructedParticle::get_phi(sel_leptons)")
            .Define("charge_leptons",  "FCCAnalyses::ReconstructedParticle::get_charge(sel_leptons)")
            # first four leptons
            # leading lepton
            .Define("E_l1", "(n_leptons > 0) ? E_leptons[0] : -999.")
            .Define("pT_l1", "(n_leptons > 0) ? pT_leptons[0] : -999.")
            .Define("eta_l1", "(n_leptons > 0) ? eta_leptons[0] : -999.")
            .Define("phi_l1", "(n_leptons > 0) ? phi_leptons[0] : -999.")
            .Define("charge_l1", "(n_leptons > 0) ? charge_leptons[0] : -999.")
            .Define("idx_l1", "(n_leptons > 0) ? idx_leptons[0] : -999.")
            # subleading lepton
            .Define("E_l2", "(n_leptons > 1) ? E_leptons[1] : -999.")
            .Define("pT_l2", "(n_leptons > 1) ? pT_leptons[1] : -999.")
            .Define("eta_l2", "(n_leptons > 1) ? eta_leptons[1] : -999.")
            .Define("phi_l2", "(n_leptons > 1) ? phi_leptons[1] : -999.")
            .Define("charge_l2", "(n_leptons > 1) ? charge_leptons[1] : -999.")
            .Define("idx_l2", "(n_leptons > 1) ? idx_leptons[1] : -999.")
            # third lepton
            .Define("E_l3", "(n_leptons > 2) ? E_leptons[2] : -999.")
            .Define("pT_l3", "(n_leptons > 2) ? pT_leptons[2] : -999.")
            .Define("eta_l3", "(n_leptons > 2) ? eta_leptons[2] : -999.")
            .Define("phi_l3", "(n_leptons > 2) ? phi_leptons[2] : -999.")
            .Define("charge_l3", "(n_leptons > 2) ? charge_leptons[2] : -999.")
            .Define("idx_l3", "(n_leptons > 2) ? idx_leptons[2] : -999.")
            # fourth lepton
            .Define("E_l4", "(n_leptons > 3) ? E_leptons[3] : -999.")
            .Define("pT_l4", "(n_leptons > 3) ? pT_leptons[3] : -999.")
            .Define("eta_l4", "(n_leptons > 3) ? eta_leptons[3] : -999.")
            .Define("phi_l4", "(n_leptons > 3) ? phi_leptons[3] : -999.")
            .Define("charge_l4", "(n_leptons > 3) ? charge_leptons[3] : -999.")
            .Define("idx_l4", "(n_leptons > 3) ? idx_leptons[3] : -999.")
            # Reco-to-MC particle association for the four leptons (print only PDGID)
            .Define("pdgID_l1", "(idx_l1 >= 0 && idx_l1 < RP2MC_index.size() ) ? Particle.at(RP2MC_index[idx_l1]).PDG : -999")
            .Define("pdgID_l2", "(idx_l2 >= 0 && idx_l2 < RP2MC_index.size() ) ? Particle.at(RP2MC_index[idx_l2]).PDG : -999")
            .Define("pdgID_l3", "(idx_l3 >= 0 && idx_l3 < RP2MC_index.size() ) ? Particle.at(RP2MC_index[idx_l3]).PDG : -999")
            .Define("pdgID_l4", "(idx_l4 >= 0 && idx_l4 < RP2MC_index.size() ) ? Particle.at(RP2MC_index[idx_l4]).PDG : -999")
            # check which lepton is the Z boson decay product
            .Define("is_from_Z_l1", "(idx_l1 >= 0) ? (idx_l1 == idx_e1) || (idx_l1 == idx_e2) : false")
            .Define("is_from_Z_l2", "(idx_l2 >= 0) ? (idx_l2 == idx_e1) || (idx_l2 == idx_e2) : false")
            .Define("is_from_Z_l3", "(idx_l3 >= 0) ? (idx_l3 == idx_e1) || (idx_l3 == idx_e2) : false")
            .Define("is_from_Z_l4", "(idx_l4 >= 0) ? (idx_l4 == idx_e1) || (idx_l4 == idx_e2) : false")
            # invariant mass combinations and pT for the two leptons from the Z boson   
            .Define("m_ll", "(idx_l1 >= 0 && idx_l2 >= 0) ? (lepton_tlv.at(0) + lepton_tlv.at(1)).M() : -999.")
            .Define("pT_ll", "(idx_l1 >= 0 && idx_l2 >= 0) ? (lepton_tlv.at(0) + lepton_tlv.at(1)).Pt() : -999.")
            # get the invariant mass of the lepton pair NOT from the Z boson
            .Define("m_ll_non_Z", "(idx_l3 >= 0 && idx_l4 >= 0) ? (lepton_tlv.at(2) + lepton_tlv.at(3)).M() : -999.")
            .Define("pT_ll_non_Z", "(idx_l3 >= 0 && idx_l4 >= 0) ? (lepton_tlv.at(2) + lepton_tlv.at(3)).Pt() : -999.")
            .Define("DR_l_l_non_Z", "(idx_l3 >= 0 && idx_l4 >= 0) ? lepton_tlv.at(2).DeltaR(lepton_tlv.at(3)) : -999.")

            # sum of the charge of the first four leptons
            .Define("sum_charge_leptons", "(n_leptons >= 4) ? charge_l1 + charge_l2 + charge_l3 + charge_l4 : -999.")
            ########################################### JETS ########################################### 
            # get jets and their indices
            .Define("idx_jets", "FCCAnalyses::ReconstructedParticle::get_idx(Jet)")
            # select jets with pT > 25 GeV
            .Define("selpt_jets", "FCCAnalyses::ReconstructedParticle::sel_pt({jet_pt})(Jet)".format(jet_pt=self.ana_args.jet_pt))
            .Define("idx_selpt_jets", "FCCAnalyses::ReconstructedParticle::sel_pt({jet_pt})(Jet,idx_jets)".format(jet_pt=self.ana_args.jet_pt))
            # sort jets by pT
            .Define("sel_jets", "AnalysisFCChh::SortParticleCollection(selpt_jets)") 
            .Define("idx_sel_jets", "AnalysisFCChh::SortParticleCollection(selpt_jets, idx_selpt_jets)")
            # output branches
            .Define("n_jets",  "FCCAnalyses::ReconstructedParticle::get_n(sel_jets)")
            .Define("E_jets",  "FCCAnalyses::ReconstructedParticle::get_e(sel_jets)")
            .Define("pT_jets",  "FCCAnalyses::ReconstructedParticle::get_pt(sel_jets)")
            .Define("eta_jets",  "FCCAnalyses::ReconstructedParticle::get_eta(sel_jets)")
            .Define("phi_jets",  "FCCAnalyses::ReconstructedParticle::get_phi(sel_jets)")
            # b-tagging information
            .Define("pass_loose_btag_jets", "AnalysisFCChh::get_pass_tag(Jet, idx_sel_jets, Jet_HF_tags, _Jet_HF_tags_particle, _Jet_HF_tags_parameters, 0)") #bit 0 = loose WP, see: https://github.com/delphes/delphes/blob/master/cards/FCC/scenarios/FCChh_I.tcl
            .Define("pass_medium_btag_jets", "AnalysisFCChh::get_pass_tag(Jet, idx_sel_jets, Jet_HF_tags, _Jet_HF_tags_particle, _Jet_HF_tags_parameters, 1)") #bit 1 = medium WP, see: https://github.com/delphes/delphes/blob/master/cards/FCC/scenarios/FCChh_I.tcl
            .Define("pass_tight_btag_jets", "AnalysisFCChh::get_pass_tag(Jet, idx_sel_jets, Jet_HF_tags, _Jet_HF_tags_particle, _Jet_HF_tags_parameters, 2)") #bit 2 = tight WP, see: https://github.com/delphes/delphes/blob/master/cards/FCC/scenarios/FCChh_I.tcl
            .Define("btag_score_jets", "AnalysisFCChh::get_btagging_score(pass_loose_btag_jets, pass_medium_btag_jets, pass_tight_btag_jets)") 
            # first six jets
            # leading jet
            .Define("E_j1", "(n_jets > 0) ? E_jets[0] : -999.")
            .Define("pT_j1", "(n_jets > 0) ? pT_jets[0] : -999.")
            .Define("eta_j1", "(n_jets > 0) ? eta_jets[0] : -999.")
            .Define("phi_j1", "(n_jets > 0) ? phi_jets[0] : -999.")
            .Define("pass_loose_btag_j1", "(n_jets > 0) ? pass_loose_btag_jets[0] : -999.")
            .Define("pass_medium_btag_j1", "(n_jets > 0) ? pass_medium_btag_jets[0] : -999.")
            .Define("pass_tight_btag_j1", "(n_jets > 0) ? pass_tight_btag_jets[0] : -999.")
            .Define("btag_score_j1", "(n_jets > 0) ? btag_score_jets[0] : -999.")
            # subleading jet
            .Define("E_j2", "(n_jets > 1) ? E_jets[1] : -999.")
            .Define("pT_j2", "(n_jets > 1) ? pT_jets[1] : -999.")
            .Define("eta_j2", "(n_jets > 1) ? eta_jets[1] : -999.")
            .Define("phi_j2", "(n_jets > 1) ? phi_jets[1] : -999.")
            .Define("pass_loose_btag_j2", "(n_jets > 1) ? pass_loose_btag_jets[1] : -999.")
            .Define("pass_medium_btag_j2", "(n_jets > 1) ? pass_medium_btag_jets[1] : -999.")
            .Define("pass_tight_btag_j2", "(n_jets > 1) ? pass_tight_btag_jets[1] : -999.")
            .Define("btag_score_j2", "(n_jets > 1) ? btag_score_jets[1] : -999.")
            # 3-rd jet
            .Define("E_j3", "(n_jets > 2) ? E_jets[2] : -999.")
            .Define("pT_j3", "(n_jets > 2) ? pT_jets[2] : -999.")
            .Define("eta_j3", "(n_jets > 2) ? eta_jets[2] : -999.")
            .Define("phi_j3", "(n_jets > 2) ? phi_jets[2] : -999.")
            .Define("pass_loose_btag_j3", "(n_jets > 2) ? pass_loose_btag_jets[2] : -999.")
            .Define("pass_medium_btag_j3", "(n_jets > 2) ? pass_medium_btag_jets[2] : -999.")
            .Define("pass_tight_btag_j3", "(n_jets > 2) ? pass_tight_btag_jets[2] : -999.")
            .Define("btag_score_j3", "(n_jets > 2) ? btag_score_jets[2] : -999.")
            # 4-th jet
            .Define("E_j4", "(n_jets > 3) ? E_jets[3] : -999.")
            .Define("pT_j4", "(n_jets > 3) ? pT_jets[3] : -999.")
            .Define("eta_j4", "(n_jets > 3) ? eta_jets[3] : -999.")
            .Define("phi_j4", "(n_jets > 3) ? phi_jets[3] : -999.")
            .Define("pass_loose_btag_j4", "(n_jets > 3) ? pass_loose_btag_jets[3] : -999.")
            .Define("pass_medium_btag_j4", "(n_jets > 3) ? pass_medium_btag_jets[3] : -999.")
            .Define("pass_tight_btag_j4", "(n_jets > 3) ? pass_tight_btag_jets[3] : -999.")
            .Define("btag_score_j4", "(n_jets > 3) ? btag_score_jets[3] : -999.")
            # 5-th jet
            .Define("E_j5", "(n_jets > 4) ? E_jets[4] : -999.")
            .Define("pT_j5", "(n_jets > 4) ? pT_jets[4] : -999.")
            .Define("eta_j5", "(n_jets > 4) ? eta_jets[4] : -999.")
            .Define("phi_j5", "(n_jets > 4) ? phi_jets[4] : -999.")
            .Define("pass_loose_btag_j5", "(n_jets > 4) ? pass_loose_btag_jets[4] : -999.")
            .Define("pass_medium_btag_j5", "(n_jets > 4) ? pass_medium_btag_jets[4] : -999.")
            .Define("pass_tight_btag_j5", "(n_jets > 4) ? pass_tight_btag_jets[4] : -999.")
            .Define("btag_score_j5", "(n_jets > 4) ? btag_score_jets[4] : -999.")
            # 6-th jet
            .Define("E_j6", "(n_jets > 5) ? E_jets[5] : -999.")
            .Define("pT_j6", "(n_jets > 5) ? pT_jets[5] : -999.")
            .Define("eta_j6", "(n_jets > 5) ? eta_jets[5] : -999.")
            .Define("phi_j6", "(n_jets > 5) ? phi_jets[5] : -999.")
            .Define("pass_loose_btag_j6", "(n_jets > 5) ? pass_loose_btag_jets[5] : -999.")
            .Define("pass_medium_btag_j6", "(n_jets > 5) ? pass_medium_btag_jets[5] : -999.")
            .Define("pass_tight_btag_j6", "(n_jets > 5) ? pass_tight_btag_jets[5] : -999.")
            .Define("btag_score_j6", "(n_jets > 5) ? btag_score_jets[5] : -999.")
            # selected central jets (|eta| < 2.5)
            .Define("central_jets_unsort", "FCCAnalyses::ReconstructedParticle::sel_eta(2.5)(selpt_jets)")
            .Define("central_jets", "AnalysisFCChh::SortParticleCollection(central_jets_unsort)") 
            .Define("n_central_jets",  "FCCAnalyses::ReconstructedParticle::get_n(central_jets)")
            # get jets passing medium b-tagging
            .Define("b_tagged_jets", "AnalysisFCChh::get_tagged_jets(Jet, Jet_HF_tags, _Jet_HF_tags_particle, _Jet_HF_tags_parameters, 1)")
            .Define("idx_b_tagged_jets",  "AnalysisFCChh::get_tagged_jets_idx(Jet, Jet_HF_tags, _Jet_HF_tags_particle, _Jet_HF_tags_parameters, 1)")
            # select jets with pT > 25 GeV
            .Define("sel_bjets", "FCCAnalyses::ReconstructedParticle::sel_pt({jet_pt})(b_tagged_jets)".format(jet_pt=self.ana_args.jet_pt))
            .Define("idx_sel_bjets", "FCCAnalyses::ReconstructedParticle::sel_pt({jet_pt})(b_tagged_jets, idx_b_tagged_jets)".format(jet_pt=self.ana_args.jet_pt))
            # save output branches
            .Define("n_bjets", "FCCAnalyses::ReconstructedParticle::get_n(sel_bjets)")
            .Define("E_bjets",  "FCCAnalyses::ReconstructedParticle::get_e(sel_bjets)")
            .Define("pT_bjets",  "FCCAnalyses::ReconstructedParticle::get_pt(sel_bjets)")
            .Define("eta_bjets",  "FCCAnalyses::ReconstructedParticle::get_eta(sel_bjets)")
            .Define("phi_bjets",  "FCCAnalyses::ReconstructedParticle::get_phi(sel_bjets)")
            .Define("pass_loose_btag_bjets", "AnalysisFCChh::get_pass_tag(Jet, idx_sel_bjets, Jet_HF_tags, _Jet_HF_tags_particle, _Jet_HF_tags_parameters, 0)")
            .Define("pass_medium_btag_bjets", "AnalysisFCChh::get_pass_tag(Jet, idx_sel_bjets, Jet_HF_tags, _Jet_HF_tags_particle, _Jet_HF_tags_parameters, 1)") 
            .Define("pass_tight_btag_bjets", "AnalysisFCChh::get_pass_tag(Jet, idx_sel_bjets, Jet_HF_tags, _Jet_HF_tags_particle, _Jet_HF_tags_parameters, 2)") 
            .Define("btag_score_bjets", "AnalysisFCChh::get_btagging_score(pass_loose_btag_bjets, pass_medium_btag_bjets, pass_tight_btag_bjets)") 
            ### the first two b-jets are the ones from the top quarks
            ### leading b-jet
            .Define("E_b1", "(n_bjets > 0) ? E_bjets[0] : -999.")
            .Define("pT_b1", "(n_bjets > 0) ? pT_bjets[0] : -999.")
            .Define("eta_b1", "(n_bjets > 0) ? eta_bjets[0] : -999.")
            .Define("phi_b1", "(n_bjets > 0) ? phi_bjets[0] : -999.")
            .Define("pass_loose_btag_b1", "(n_bjets > 0) ? pass_loose_btag_bjets[0] : -999.")
            .Define("pass_medium_btag_b1", "(n_bjets > 0) ? pass_medium_btag_bjets[0] : -999.")
            .Define("pass_tight_btag_b1", "(n_bjets > 0) ? pass_tight_btag_bjets[0] : -999.")
            .Define("btag_score_b1", "(n_bjets > 0) ? btag_score_bjets[0] : -999.")
            ### subleading b-jet
            .Define("E_b2", "(n_bjets > 1) ? E_bjets[1] : -999.")
            .Define("pT_b2", "(n_bjets > 1) ? pT_bjets[1] : -999.")
            .Define("eta_b2", "(n_bjets > 1) ? eta_bjets[1] : -999.")
            .Define("phi_b2", "(n_bjets > 1) ? phi_bjets[1] : -999.")
            .Define("pass_loose_btag_b2", "(n_bjets > 1) ? pass_loose_btag_bjets[1] : -999.")
            .Define("pass_medium_btag_b2", "(n_bjets > 1) ? pass_medium_btag_bjets[1] : -999.")
            .Define("pass_tight_btag_b2", "(n_bjets > 1) ? pass_tight_btag_bjets[1] : -999.")
            .Define("btag_score_b2", "(n_bjets > 1) ? btag_score_bjets[1] : -999.")
            ### check how many medium b-jets there are
            .Define("n_medium_bjets", "std::count(pass_medium_btag_bjets.begin(), pass_medium_btag_bjets.end(), true);")
            .Define("n_loose_bjets", "std::count(pass_loose_btag_bjets.begin(), pass_loose_btag_bjets.end(), true);")
            .Define("n_tight_bjets", "std::count(pass_tight_btag_bjets.begin(), pass_tight_btag_bjets.end(), true);")
            ### bb object
            .Define("b1", "n_bjets > 0 ? FCCAnalyses::ReconstructedParticle::get_tlv(sel_bjets.at(0)) : TLorentzVector(0.,0.,0.,0.)")
            .Define("b2", "n_bjets > 1 ? FCCAnalyses::ReconstructedParticle::get_tlv(sel_bjets.at(1)) : TLorentzVector(0.,0.,0.,0.)")
            .Define("m_bb", "n_bjets > 1 ? (b1+b2).M() : -999.")
            .Define("pT_bb", "n_bjets > 1 ? (b1+b2).Pt() : -999.")
            ### get light jets
            ### assume that the first two jets are the b-jets from the top quark
            .Define("helper", "(sel_bjets.size()>1) ? 2-sel_bjets.size() : 0")
            .Define("sel_light_jets_unsorted", "ROOT::VecOps::Take(sel_bjets, helper)")
            .Define("idx_light_jets_unsorted", "ROOT::VecOps::Take(idx_sel_bjets, helper)")
            ### sort light jets by pT
            .Define("sel_light_jets", "AnalysisFCChh::SortParticleCollection(sel_light_jets_unsorted)")
            .Define("idx_sel_light_jets", "AnalysisFCChh::SortParticleCollection(sel_light_jets_unsorted, idx_light_jets_unsorted)")
            ### output branches
            .Define("n_light_jets", "FCCAnalyses::ReconstructedParticle::get_n(sel_light_jets)")
            .Define("E_light_jets",  "FCCAnalyses::ReconstructedParticle::get_e(sel_light_jets)")
            .Define("pT_light_jets",  "FCCAnalyses::ReconstructedParticle::get_pt(sel_light_jets)")
            .Define("eta_light_jets",  "FCCAnalyses::ReconstructedParticle::get_eta(sel_light_jets)")
            .Define("phi_light_jets",  "FCCAnalyses::ReconstructedParticle::get_phi(sel_light_jets)")
            .Define("pass_loose_btag_light_jets", "AnalysisFCChh::get_pass_tag(Jet, idx_sel_light_jets, Jet_HF_tags, _Jet_HF_tags_particle, _Jet_HF_tags_parameters, 0)")
            .Define("pass_medium_btag_light_jets", "AnalysisFCChh::get_pass_tag(Jet, idx_sel_light_jets, Jet_HF_tags, _Jet_HF_tags_particle, _Jet_HF_tags_parameters, 1)")
            .Define("pass_tight_btag_light_jets", "AnalysisFCChh::get_pass_tag(Jet, idx_sel_light_jets, Jet_HF_tags, _Jet_HF_tags_particle, _Jet_HF_tags_parameters, 2)")
            .Define("btag_score_light_jets", "AnalysisFCChh::get_btagging_score(pass_loose_btag_light_jets, pass_medium_btag_light_jets, pass_tight_btag_light_jets)")
            # first five light jets
            # leading light jet
            .Define("E_light1", "(n_light_jets > 0) ? E_light_jets[0] : -999.")
            .Define("pT_light1", "(n_light_jets > 0) ? pT_light_jets[0] : -999.")
            .Define("eta_light1", "(n_light_jets > 0) ? eta_light_jets[0] : -999.")
            .Define("phi_light1", "(n_light_jets > 0) ? phi_light_jets[0] : -999.")
            .Define("pass_loose_btag_light1", "(n_light_jets > 0) ? pass_loose_btag_light_jets[0] : -999.")
            .Define("pass_medium_btag_light1", "(n_light_jets > 0) ? pass_medium_btag_light_jets[0] : -999.")
            .Define("pass_tight_btag_light1", "(n_light_jets > 0) ? pass_tight_btag_light_jets[0] : -999.")
            .Define("btag_score_light1", "(n_light_jets > 0) ? btag_score_light_jets[0] : -999.")
            # subleading light jet
            .Define("E_light2", "(n_light_jets > 1) ? E_light_jets[1] : -999.")
            .Define("pT_light2", "(n_light_jets > 1) ? pT_light_jets[1] : -999.")
            .Define("eta_light2", "(n_light_jets > 1) ? eta_light_jets[1] : -999.")
            .Define("phi_light2", "(n_light_jets > 1) ? phi_light_jets[1] : -999.")
            .Define("pass_loose_btag_light2", "(n_light_jets > 1) ? pass_loose_btag_light_jets[1] : -999.")
            .Define("pass_medium_btag_light2", "(n_light_jets > 1) ? pass_medium_btag_light_jets[1] : -999.")
            .Define("pass_tight_btag_light2", "(n_light_jets > 1) ? pass_tight_btag_light_jets[1] : -999.")
            .Define("btag_score_light2", "(n_light_jets > 1) ? btag_score_light_jets[1] : -999.")
            # 3-rd light jet
            .Define("E_light3", "(n_light_jets > 2) ? E_light_jets[2] : -999.")
            .Define("pT_light3", "(n_light_jets > 2) ? pT_light_jets[2] : -999.")
            .Define("eta_light3", "(n_light_jets > 2) ? eta_light_jets[2] : -999.")
            .Define("phi_light3", "(n_light_jets > 2) ? phi_light_jets[2] : -999.")
            .Define("pass_loose_btag_light3", "(n_light_jets > 2) ? pass_loose_btag_light_jets[2] : -999.")
            .Define("pass_medium_btag_light3", "(n_light_jets > 2) ? pass_medium_btag_light_jets[2] : -999.")
            .Define("pass_tight_btag_light3", "(n_light_jets > 2) ? pass_tight_btag_light_jets[2] : -999.")
            .Define("btag_score_light3", "(n_light_jets > 2) ? btag_score_light_jets[2] : -999.")
            # 4-th light jet
            .Define("E_light4", "(n_light_jets > 3) ? E_light_jets[3] : -999.")
            .Define("pT_light4", "(n_light_jets > 3) ? pT_light_jets[3] : -999.")
            .Define("eta_light4", "(n_light_jets > 3) ? eta_light_jets[3] : -999.")
            .Define("phi_light4", "(n_light_jets > 3) ? phi_light_jets[3] : -999.")
            .Define("pass_loose_btag_light4", "(n_light_jets > 3) ? pass_loose_btag_light_jets[3] : -999.")
            .Define("pass_medium_btag_light4", "(n_light_jets > 3) ? pass_medium_btag_light_jets[3] : -999.")
            .Define("pass_tight_btag_light4", "(n_light_jets > 3) ? pass_tight_btag_light_jets[3] : -999.")
            .Define("btag_score_light4", "(n_light_jets > 3) ? btag_score_light_jets[3] : -999.")
            # 5-th light jet
            .Define("E_light5", "(n_light_jets > 4) ? E_light_jets[4] : -999.")
            .Define("pT_light5", "(n_light_jets > 4) ? pT_light_jets[4] : -999.")
            .Define("eta_light5", "(n_light_jets > 4) ? eta_light_jets[4] : -999.")
            .Define("phi_light5", "(n_light_jets > 4) ? phi_light_jets[4] : -999.")
            .Define("pass_loose_btag_light5", "(n_light_jets > 4) ? pass_loose_btag_light_jets[4] : -999.")
            .Define("pass_medium_btag_light5", "(n_light_jets > 4) ? pass_medium_btag_light_jets[4] : -999.")
            .Define("pass_tight_btag_light5", "(n_light_jets > 4) ? pass_tight_btag_light_jets[4] : -999.")
            .Define("btag_score_light5", "(n_light_jets > 4) ? btag_score_light_jets[4] : -999.")
            # scalar sum of all jet's momenta
            .Define("HT", "AnalysisFCChh::get_HT_jets(Jet)")
            # topness
            .Define("topness", "(n_bjets > 0) ? AnalysisFCChh::get_topness(sel_jets) : -999.")
            # get the jets from the hadronic top decay
            .Define("top_had_jet_idx", "(n_bjets > 0) ? AnalysisFCChh::get_topness_jets(sel_jets) : ROOT::VecOps::RVec<int>(0)")
            .Define("top_had_jet_idx_1", "(top_had_jet_idx.size() > 2) ? top_had_jet_idx.at(0) : -1")
            .Define("top_had_jet_idx_2", "(top_had_jet_idx.size() > 2) ? top_had_jet_idx.at(1) : -1")
            .Define("top_had_jet_idx_3", "(top_had_jet_idx.size() > 2) ? top_had_jet_idx.at(2) : -1")
            .Define("top_had_jet1_tlv", "(n_jets > 0 && top_had_jet_idx_1 >=0 && n_jets > top_had_jet_idx_1) ? FCCAnalyses::ReconstructedParticle::get_tlv(sel_jets.at(top_had_jet_idx_1)) : TLorentzVector(0.,0.,0.,0.)")
            .Define("top_had_jet2_tlv", "(n_jets > 0 && top_had_jet_idx_2 >=0 && n_jets > top_had_jet_idx_2) ? FCCAnalyses::ReconstructedParticle::get_tlv(sel_jets.at(top_had_jet_idx_2)) : TLorentzVector(0.,0.,0.,0.)")
            .Define("top_had_jet3_tlv", "(n_jets > 0 && top_had_jet_idx_3 >=0 && n_jets > top_had_jet_idx_3) ? FCCAnalyses::ReconstructedParticle::get_tlv(sel_jets.at(top_had_jet_idx_3)) : TLorentzVector(0.,0.,0.,0.)")
            .Define("E_top_had_jet1", "(n_jets > top_had_jet_idx_1) ? E_jets[top_had_jet_idx_1] : -999.")
            .Define("pT_top_had_jet1", "(n_jets > top_had_jet_idx_1) ? pT_jets[top_had_jet_idx_1] : -999.")
            .Define("eta_top_had_jet1", "(n_jets > top_had_jet_idx_1) ? eta_jets[top_had_jet_idx_1] : -999.")
            .Define("phi_top_had_jet1", "(n_jets > top_had_jet_idx_1) ? phi_jets[top_had_jet_idx_1] : -999.")
            .Define("pass_loose_btag_top_had_jet1", "(n_jets > top_had_jet_idx_1) ? pass_loose_btag_jets[top_had_jet_idx_1] : -999.")
            .Define("pass_medium_btag_top_had_jet1", "(n_jets > top_had_jet_idx_1) ? pass_medium_btag_jets[top_had_jet_idx_1] : -999.")
            .Define("pass_tight_btag_top_had_jet1", "(n_jets > top_had_jet_idx_1) ? pass_tight_btag_jets[top_had_jet_idx_1] : -999.")
            .Define("btag_score_top_had_jet1", "(n_jets > top_had_jet_idx_1) ? btag_score_jets[top_had_jet_idx_1] : -999.")
            .Define("E_top_had_jet2", "(n_jets > top_had_jet_idx_2) ? E_jets[top_had_jet_idx_2] : -999.")
            .Define("pT_top_had_jet2", "(n_jets > top_had_jet_idx_2) ? pT_jets[top_had_jet_idx_2] : -999.")
            .Define("eta_top_had_jet2", "(n_jets > top_had_jet_idx_2) ? eta_jets[top_had_jet_idx_2] : -999.")
            .Define("phi_top_had_jet2", "(n_jets > top_had_jet_idx_2) ? phi_jets[top_had_jet_idx_2] : -999.")
            .Define("pass_loose_btag_top_had_jet2", "(n_jets > top_had_jet_idx_2) ? pass_loose_btag_jets[top_had_jet_idx_2] : -999.")
            .Define("pass_medium_btag_top_had_jet2", "(n_jets > top_had_jet_idx_2) ? pass_medium_btag_jets[top_had_jet_idx_2] : -999.")
            .Define("pass_tight_btag_top_had_jet2", "(n_jets > top_had_jet_idx_2) ? pass_tight_btag_jets[top_had_jet_idx_2] : -999.")
            .Define("btag_score_top_had_jet2", "(n_jets > top_had_jet_idx_2) ? btag_score_jets[top_had_jet_idx_2] : -999.")
            .Define("E_top_had_jet3", "(n_jets > top_had_jet_idx_3) ? E_jets[top_had_jet_idx_3] : -999.")
            .Define("pT_top_had_jet3", "(n_jets > top_had_jet_idx_3) ? pT_jets[top_had_jet_idx_3] : -999.")
            .Define("eta_top_had_jet3", "(n_jets > top_had_jet_idx_3) ? eta_jets[top_had_jet_idx_3] : -999.")
            .Define("phi_top_had_jet3", "(n_jets > top_had_jet_idx_3) ? phi_jets[top_had_jet_idx_3] : -999.")
            .Define("pass_loose_btag_top_had_jet3", "(n_jets > top_had_jet_idx_3) ? pass_loose_btag_jets[top_had_jet_idx_3] : -999.")
            .Define("pass_medium_btag_top_had_jet3", "(n_jets > top_had_jet_idx_3) ? pass_medium_btag_jets[top_had_jet_idx_3] : -999.")
            .Define("pass_tight_btag_top_had_jet3", "(n_jets > top_had_jet_idx_3) ? pass_tight_btag_jets[top_had_jet_idx_3] : -999.")
            .Define("btag_score_top_had_jet3", "(n_jets > top_had_jet_idx_3) ? btag_score_jets[top_had_jet_idx_3] : -999.")
            # reonctruct the W decay and top decay in case of hadronic top
            # using the three jets extracted from the topness calculation
            .Define("m_w_had", "(n_jets > 2) ? (top_had_jet2_tlv+top_had_jet3_tlv).M() : -999.")
            .Define("pT_w_had", "(n_jets > 2) ? (top_had_jet2_tlv+top_had_jet3_tlv).Pt() : -999.")
            .Define("eta_w_had", "(n_jets > 2) ? (top_had_jet2_tlv+top_had_jet3_tlv).Eta() : -999.")
            .Define("phi_w_had", "(n_jets > 2) ? (top_had_jet2_tlv+top_had_jet3_tlv).Phi() : -999.")
            .Define("E_w_had", "(n_jets > 2) ? (top_had_jet2_tlv+top_had_jet3_tlv).E() : -999.")
            .Define("m_top_had", "(n_jets > 2) ? (top_had_jet1_tlv+top_had_jet2_tlv+top_had_jet3_tlv).M() : -999.")
            .Define("pT_top_had", "(n_jets > 2) ? (top_had_jet1_tlv+top_had_jet2_tlv+top_had_jet3_tlv).Pt() : -999.")
            .Define("eta_top_had", "(n_jets > 2) ? (top_had_jet1_tlv+top_had_jet2_tlv+top_had_jet3_tlv).Eta() : -999.")
            .Define("phi_top_had", "(n_jets > 2) ? (top_had_jet1_tlv+top_had_jet2_tlv+top_had_jet3_tlv).Phi() : -999.")
            # the first index is the index of the b-jet
            # it can be either the leading or the subleading b-jet (passing the medium b-tagging)
            # the second and third indices are the indices of the light jets from the W in case of the hadronic top
            # get the invariant mass of the two b-jets and the two leptons
            .Define("m_b1l3", "(n_bjets > 0 && n_leptons > 2) ? (FCCAnalyses::ReconstructedParticle::get_tlv(sel_bjets[0]) + FCCAnalyses::ReconstructedParticle::get_tlv(sel_leptons[3])).M() : -999.")
            .Define("m_b1l4", "(n_bjets > 0 && n_leptons > 3) ? (FCCAnalyses::ReconstructedParticle::get_tlv(sel_bjets[0]) + FCCAnalyses::ReconstructedParticle::get_tlv(sel_leptons[4])).M() : -999.")
            .Define("m_b2l3", "(n_bjets > 1 && n_leptons > 2) ? (FCCAnalyses::ReconstructedParticle::get_tlv(sel_bjets[1]) + FCCAnalyses::ReconstructedParticle::get_tlv(sel_leptons[3])).M() : -999.")
            .Define("m_b2l4", "(n_bjets > 1 && n_leptons > 3) ? (FCCAnalyses::ReconstructedParticle::get_tlv(sel_bjets[1]) + FCCAnalyses::ReconstructedParticle::get_tlv(sel_leptons[4])).M() : -999.")
            .Define("m_b1l", "(n_bjets > 0 && n_leptons > 2) ? (( sqrt(pow(m_b1l3, 2)+pow(m_b2l4, 2)) <= sqrt(pow(m_b1l4, 2)+pow(m_b2l3, 2)) ? m_b1l3 : m_b1l4 )) : -999.")
            .Define("m_b2l", "(n_bjets > 0 && n_leptons > 2) ? (( sqrt(pow(m_b1l3, 2)+pow(m_b2l4, 2)) <= sqrt(pow(m_b1l4, 2)+pow(m_b2l3, 2)) ? m_b2l4 : m_b2l3 )) : -999.")
            # delta R between photons and jets
            .Define("DR_y1_j1", "(n_photons > 0 && n_jets > 0) ? FCCAnalyses::ReconstructedParticle::get_tlv(sel_gamma[0]).DeltaR(FCCAnalyses::ReconstructedParticle::get_tlv(sel_jets[0])) : -999.")
            .Define("DR_y1_j2", "(n_photons > 0 && n_jets > 1) ? FCCAnalyses::ReconstructedParticle::get_tlv(sel_gamma[0]).DeltaR(FCCAnalyses::ReconstructedParticle::get_tlv(sel_jets[1])) : -999.")
            .Define("DR_y2_j1", "(n_photons > 1 && n_jets > 0) ? FCCAnalyses::ReconstructedParticle::get_tlv(sel_gamma[1]).DeltaR(FCCAnalyses::ReconstructedParticle::get_tlv(sel_jets[0])) : -999.")
            .Define("DR_y2_j2", "(n_photons > 1 && n_jets > 1) ? FCCAnalyses::ReconstructedParticle::get_tlv(sel_gamma[1]).DeltaR(FCCAnalyses::ReconstructedParticle::get_tlv(sel_jets[1])) : -999.")
            # delta R between photons and b-jets
            .Define("DR_y1_b1", "(n_photons > 0 && n_bjets > 0) ? FCCAnalyses::ReconstructedParticle::get_tlv(sel_gamma[0]).DeltaR(FCCAnalyses::ReconstructedParticle::get_tlv(sel_bjets[0])) : -999.")
            .Define("DR_y1_b2", "(n_photons > 0 && n_bjets > 1) ? FCCAnalyses::ReconstructedParticle::get_tlv(sel_gamma[0]).DeltaR(FCCAnalyses::ReconstructedParticle::get_tlv(sel_bjets[1])) : -999.")
            .Define("DR_y2_b1", "(n_photons > 1 && n_bjets > 0) ? FCCAnalyses::ReconstructedParticle::get_tlv(sel_gamma[1]).DeltaR(FCCAnalyses::ReconstructedParticle::get_tlv(sel_bjets[0])) : -999.")
            .Define("DR_y2_b2", "(n_photons > 1 && n_bjets > 1) ? FCCAnalyses::ReconstructedParticle::get_tlv(sel_gamma[1]).DeltaR(FCCAnalyses::ReconstructedParticle::get_tlv(sel_bjets[1])) : -999.")
            ## # delta R between the two b-jets
            .Define("DR_b_b", "(n_bjets > 1) ? FCCAnalyses::ReconstructedParticle::get_tlv(sel_bjets[0]).DeltaR(FCCAnalyses::ReconstructedParticle::get_tlv(sel_bjets[1])) : -999.")
            # delta R between the two b-jets and the four leptons
            .Define("DR_b1_l1", "(n_bjets > 0 && n_leptons > 0) ? FCCAnalyses::ReconstructedParticle::get_tlv(sel_bjets[0]).DeltaR(FCCAnalyses::ReconstructedParticle::get_tlv(sel_leptons[0])) : -999.")
            .Define("DR_b1_l2", "(n_bjets > 0 && n_leptons > 1) ? FCCAnalyses::ReconstructedParticle::get_tlv(sel_bjets[0]).DeltaR(FCCAnalyses::ReconstructedParticle::get_tlv(sel_leptons[1])) : -999.")
            .Define("DR_b1_l3", "(n_bjets > 0 && n_leptons > 2) ? FCCAnalyses::ReconstructedParticle::get_tlv(sel_bjets[0]).DeltaR(FCCAnalyses::ReconstructedParticle::get_tlv(sel_leptons[2])) : -999.")
            .Define("DR_b1_l4", "(n_bjets > 0 && n_leptons > 3) ? FCCAnalyses::ReconstructedParticle::get_tlv(sel_bjets[0]).DeltaR(FCCAnalyses::ReconstructedParticle::get_tlv(sel_leptons[3])) : -999.")
            .Define("DR_b2_l1", "(n_bjets > 1 && n_leptons > 0) ? FCCAnalyses::ReconstructedParticle::get_tlv(sel_bjets[1]).DeltaR(FCCAnalyses::ReconstructedParticle::get_tlv(sel_leptons[0])) : -999.")
            .Define("DR_b2_l2", "(n_bjets > 1 && n_leptons > 1) ? FCCAnalyses::ReconstructedParticle::get_tlv(sel_bjets[1]).DeltaR(FCCAnalyses::ReconstructedParticle::get_tlv(sel_leptons[1])) : -999.")
            .Define("DR_b2_l3", "(n_bjets > 1 && n_leptons > 2) ? FCCAnalyses::ReconstructedParticle::get_tlv(sel_bjets[1]).DeltaR(FCCAnalyses::ReconstructedParticle::get_tlv(sel_leptons[2])) : -999.")
            .Define("DR_b2_l4", "(n_bjets > 1 && n_leptons > 3) ? FCCAnalyses::ReconstructedParticle::get_tlv(sel_bjets[1]).DeltaR(FCCAnalyses::ReconstructedParticle::get_tlv(sel_leptons[3])) : -999.")
            ########################################### MET ########################################### 
            .Define("MET", "FCCAnalyses::ReconstructedParticle::get_pt(MissingET)")
            .Define("MET_x", "FCCAnalyses::ReconstructedParticle::get_px(MissingET)")
            .Define("MET_y", "FCCAnalyses::ReconstructedParticle::get_py(MissingET)")
            .Define("MET_phi", "FCCAnalyses::ReconstructedParticle::get_phi(MissingET)")
            ########################################### TRUTH HIGGS  ########################################### 
            .Define("higgs",  "AnalysisFCChh::get_final_Higgs(Particle, _Particle_daughters)")
            .Define("n_higgs",  "FCCAnalyses::MCParticle::get_n(higgs)")
            .Define("pT_higgs",  "FCCAnalyses::MCParticle::get_pt(higgs)")
            .Define("E_higgs",  "FCCAnalyses::MCParticle::get_e(higgs)")
            .Define("eta_higgs",  "FCCAnalyses::MCParticle::get_eta(higgs)")
            .Define("phi_higgs",  "FCCAnalyses::MCParticle::get_phi(higgs)")
            .Define("rapidity_higgs",  "FCCAnalyses::MCParticle::get_y(higgs)")
            .Define("higgs_decay_type",  "AnalysisFCChh::findHiggsDecayChannel(Particle, _Particle_daughters)")
            .Define("higgs_children",  "(n_higgs > 0) ? AnalysisFCChh::get_immediate_children(higgs.at(0), Particle, _Particle_daughters) : ROOT::VecOps::RVec<edm4hep::MCParticleData>()")
            .Define("n_higgs_children",  "FCCAnalyses::MCParticle::get_n(higgs_children)")
            .Define("higgs_child_pdgId",  "FCCAnalyses::MCParticle::get_pdg(higgs_children)")
            .Define("higgs_child1_pdgId",  "(n_higgs_children > 0) ? higgs_child_pdgId[0] : -999")
            .Define("higgs_child2_pdgId",  "(n_higgs_children > 1) ? higgs_child_pdgId[1] : -999")
            ########################################### TRUTH TOP  ########################################### 
            .Define("tops",  "AnalysisFCChh::get_final_top(Particle, _Particle_daughters)")
            .Define("n_tops",  "FCCAnalyses::MCParticle::get_n(tops)")
            .Define("pT_tops",  "FCCAnalyses::MCParticle::get_pt(tops)")
            .Define("E_tops",  "FCCAnalyses::MCParticle::get_e(tops)")
            .Define("eta_tops",  "FCCAnalyses::MCParticle::get_eta(tops)")
            .Define("phi_tops",  "FCCAnalyses::MCParticle::get_phi(tops)")
            .Define("rapidity_tops",  "FCCAnalyses::MCParticle::get_y(tops)")
            .Define("E_top1", "(n_tops > 0) ? E_tops[0] : -999.")
            .Define("pT_top1", "(n_tops > 0) ? pT_tops[0] : -999.")
            .Define("eta_top1", "(n_tops > 0) ? eta_tops[0] : -999.")
            .Define("phi_top1", "(n_tops > 0) ? phi_tops[0] : -999.")
            .Define("rapidity_top1", "(n_tops > 0) ? rapidity_tops[0] : -999.")
            .Define("E_top2", "(n_tops > 1) ? E_tops[1] : -999.")
            .Define("pT_top2", "(n_tops > 1) ? pT_tops[1] : -999.")
            .Define("eta_top2", "(n_tops > 1) ? eta_tops[1] : -999.")
            .Define("phi_top2", "(n_tops > 1) ? phi_tops[1] : -999.")
            .Define("rapidity_top2", "(n_tops > 1) ? rapidity_tops[1] : -999.")
            ########################################### TRUTH PHOTONS ########################################### 
            .Define("truth_photons", "AnalysisFCChh::get_final_photons(Particle)")
            # diphoton pair
            .Define("truth_yy_pairs_unmerged", "AnalysisFCChh::getPairs(truth_photons)") # retrieves the leading pT pair of all possible 
            .Define("truth_yy_pairs", "AnalysisFCChh::merge_pairs(truth_yy_pairs_unmerged)") # merge pair into one object to access inv masses etc
            .Define("truth_m_yy", "FCCAnalyses::MCParticle::get_mass(truth_yy_pairs)")
            # truth photons
            .Define("n_truth_photons",  "FCCAnalyses::MCParticle::get_n(truth_photons)")
            .Define("E_truth_photons",  "FCCAnalyses::MCParticle::get_e(truth_photons)")
            .Define("pT_truth_photons",  "FCCAnalyses::MCParticle::get_pt(truth_photons)")
            .Define("eta_truth_photons",  "FCCAnalyses::MCParticle::get_eta(truth_photons)")
            .Define("phi_truth_photons",  "FCCAnalyses::MCParticle::get_phi(truth_photons)")
            .Define("E_truth_y1", "(n_truth_photons > 0) ? E_truth_photons[0] : -999.")
            .Define("pT_truth_y1", "(n_truth_photons > 0) ? pT_truth_photons[0] : -999.")
            .Define("eta_truth_y1", "(n_truth_photons > 0) ? eta_truth_photons[0] : -999.")
            .Define("phi_truth_y1", "(n_truth_photons > 0) ? phi_truth_photons[0] : -999.")
            .Define("E_truth_y2", "(n_truth_photons > 1) ? E_truth_photons[1] : -999.")
            .Define("pT_truth_y2", "(n_truth_photons > 1) ? pT_truth_photons[1] : -999.")
            .Define("eta_truth_y2", "(n_truth_photons > 1) ? eta_truth_photons[1] : -999.")
            .Define("phi_truth_y2", "(n_truth_photons > 1) ? phi_truth_photons[1] : -999.")
            ############################################### TRUTH Z BOSON #############################################
            .Define("Zbosons",  "AnalysisFCChh::get_final_Zboson(Particle, _Particle_daughters)")
            .Define("n_Z",  "FCCAnalyses::MCParticle::get_n(Zbosons)")
            .Define("pT_Z",  "FCCAnalyses::MCParticle::get_pt(Zbosons)")
            .Define("E_Z",  "FCCAnalyses::MCParticle::get_e(Zbosons)")
            .Define("eta_Z",  "FCCAnalyses::MCParticle::get_eta(Zbosons)")
            .Define("phi_Z",  "FCCAnalyses::MCParticle::get_phi(Zbosons)")
            .Define("rapidity_Z",  "FCCAnalyses::MCParticle::get_y(Zbosons)")
            .Define("Z_decay_type",  "AnalysisFCChh::findZDecayChannel(Particle, _Particle_daughters)")
            .Define("Z_children",  "(n_Z > 0) ? AnalysisFCChh::get_immediate_children(Zbosons.at(0), Particle, _Particle_daughters) : ROOT::VecOps::RVec<edm4hep::MCParticleData>()")
            .Define("n_Z_children",  "FCCAnalyses::MCParticle::get_n(Z_children)")
            .Define("Z_child_pdgId",  "FCCAnalyses::MCParticle::get_pdg(higgs_children)")
            .Define("Z_child1_pdgId",  "(n_Z_children > 0) ? Z_child_pdgId[0] : -999")
            .Define("Z_child2_pdgId",  "(n_Z_children > 1) ? Z_child_pdgId[1] : -999")
            ########################################### APPLY PRE-SELECTION ########################################### 
            # require H->yy decay for signal sample
            #.Filter("higgs_decay_type==7")
        )
        return dframe2

    # Mandatory: output function, please make sure you return the branch list
    # as a python list
    def output(self):
        '''
        Output variables which will be saved to output root file.
        '''
        plain = {
            "ttH" : ['weight', 'event_number', "m_yy", "n_photons", "pT_y1", "pT_y2", "rel_pT_y1", "rel_pT_y2", "pT_yy", "n_bjets", "n_electrons", "n_muons", "rapidity_higgs", "pT_higgs", "pT_e1", "pT_mu1", "pT_l1", "pT_b1", "pT_b2"],
            "ttZ" : ['weight', 'event_number', "m_ee", "n_electrons", "pT_e1", "pT_e2", "charge_e1", "charge_e2", "n_muons", "n_leptons", "n_bjets", "n_photons", "pT_b1", "pT_b2"],
        }

        photon_list = [
            # reconstructed photons
            "n_photons", "E_photons", "pT_photons", "eta_photons", "phi_photons",
            "m_yy", "pT_yy", "rapidity_yy",
            "E_y1", "pT_y1", "eta_y1", "phi_y1", "rel_pT_y1", "idx_y1", "has_higgs_parent_y1",
            "E_y2", "pT_y2", "eta_y2", "phi_y2", "rel_pT_y2", "idx_y2", "has_higgs_parent_y2",
            "DR_y_y",
            "DR_y1_b1", "DR_y1_b2", "DR_y1_j1", "DR_y1_j2",
            "DR_y2_b1", "DR_y2_b2", "DR_y2_j1", "DR_y2_j2",
            "theta_y_y", "cos_theta_y_y",
            # reco-to-truth association for photons
            "true_E_y1", "true_pT_y1", "true_eta_y1", "true_phi_y1",
            "true_E_y2", "true_pT_y2", "true_eta_y2", "true_phi_y2",
            "pdgID_y1", "pdgID_y2",
            "true_m_yy", 'true_pT_yy', 'true_DR_y_y',
            'true_theta_y_y', 'true_cos_theta_y_y',
        ]    
        
        truth_HtoYY_list = [
            # truth photons from Higgs
            "HtoYY_n_truth_photons", "HtoYY_truth_m_yy",
            "HtoYY_E_truth_photons", "HtoYY_pT_truth_photons", "HtoYY_eta_truth_photons", "HtoYY_phi_truth_photons",
            "HtoYY_truth_E_y1", "HtoYY_truth_pT_y1", "HtoYY_truth_eta_y1", "HtoYY_truth_phi_y1",
            "HtoYY_truth_E_y2", "HtoYY_truth_pT_y2", "HtoYY_truth_eta_y2", "HtoYY_truth_phi_y2"
        ]

        lepton_list = [
            # Reconstructed electrons
            'n_electrons', 'E_electrons', 'pT_electrons', 'eta_electrons', 'phi_electrons', 
            "m_ee", "pT_ee", "DR_e_e",
            "E_e1", "pT_e1", "eta_e1", "phi_e1", "charge_e1",
            "E_e2", "pT_e2", "eta_e2", "phi_e2", "charge_e2",
            # Reconstructed muons
            'n_muons', 'E_muons', 'pT_muons', 'eta_muons', 'phi_muons',
            "m_mumu",
            "E_mu1", "pT_mu1", "eta_mu1", "phi_mu1", "charge_mu1",
            "E_mu2", "pT_mu2", "eta_mu2", "phi_mu2", "charge_mu2",
            # Reconstructed leptons (electrons + muons)
            "n_leptons", "E_leptons", "pT_leptons", "eta_leptons", "phi_leptons",
            "m_ll", "pT_ll", "m_ll_non_Z", "pT_ll_non_Z", "DR_l_l_non_Z",
            "sum_charge_leptons",
            "E_l1", "pT_l1", "eta_l1", "phi_l1", "charge_l1", "idx_l1", "pdgID_l1",
            "E_l2", "pT_l2", "eta_l2", "phi_l2", "charge_l2", "idx_l2", "pdgID_l2",
            "E_l3", "pT_l3", "eta_l3", "phi_l3", "charge_l3", "idx_l3", "pdgID_l3",
            "E_l4", "pT_l4", "eta_l4", "phi_l4", "charge_l4", "idx_l4", "pdgID_l4",
            "is_from_Z_l1", "is_from_Z_l2", "is_from_Z_l3", "is_from_Z_l4",
            # Reco-to-truth association for electrons 
            "true_E_e1", "true_pT_e1", "true_eta_e1", "true_phi_e1", "true_charge_e1",
            "true_E_e2", "true_pT_e2", "true_eta_e2", "true_phi_e2", "true_charge_e2",
            "true_m_ee", 'true_pT_ee', "true_DR_e_e",
        ]
        truth_ZtoEE_list = [
            # truth electrons from Z
            "ZtoEE_n_truth_electrons", "ZtoEE_truth_m_ee",
            "ZtoEE_E_truth_electrons", "ZtoEE_pT_truth_electrons", "ZtoEE_eta_truth_electrons", "ZtoEE_phi_truth_electrons",
            "ZtoEE_truth_E_e1", "ZtoEE_truth_pT_e1", "ZtoEE_truth_eta_e1", "ZtoEE_truth_phi_e1",
            "ZtoEE_truth_E_e2", "ZtoEE_truth_pT_e2", "ZtoEE_truth_eta_e2", "ZtoEE_truth_phi_e2"
        ]

        jet_list = [
            # Jets (ordered by pT)
            'n_jets', 'E_jets', 'pT_jets', 'eta_jets', 'phi_jets', 
            "pass_loose_btag_jets", "pass_medium_btag_jets", "pass_tight_btag_jets",
            "btag_score_jets",
             "E_j1", "pT_j1", "eta_j1", "phi_j1", "pass_loose_btag_j1", "pass_medium_btag_j1", "pass_tight_btag_j1", "btag_score_j1",
             "E_j2", "pT_j2", "eta_j2", "phi_j2", "pass_loose_btag_j2", "pass_medium_btag_j2", "pass_tight_btag_j2", "btag_score_j2",
             "E_j3", "pT_j3", "eta_j3", "phi_j3", "pass_loose_btag_j3", "pass_medium_btag_j3", "pass_tight_btag_j3", "btag_score_j3",
             "E_j4", "pT_j4", "eta_j4", "phi_j4", "pass_loose_btag_j4", "pass_medium_btag_j4", "pass_tight_btag_j4", "btag_score_j4",
             "E_j5", "pT_j5", "eta_j5", "phi_j5", "pass_loose_btag_j5", "pass_medium_btag_j5", "pass_tight_btag_j5", "btag_score_j5",
             "E_j6", "pT_j6", "eta_j6", "phi_j6", "pass_loose_btag_j6", "pass_medium_btag_j6", "pass_tight_btag_j6", "btag_score_j6",
            # Jets ordered by b-tagging score
            'n_bjets', 
            'E_bjets', 'pT_bjets', 'eta_bjets', 'phi_bjets', 
            "pass_loose_btag_bjets", "pass_medium_btag_bjets", "pass_tight_btag_bjets",
            "btag_score_bjets",
            "n_medium_bjets", "n_loose_bjets", "n_tight_bjets",
            ## # leading and subleading b-jets (ordered by pT)
            "E_b1", "pT_b1", "eta_b1", "phi_b1", "pass_loose_btag_b1", "pass_medium_btag_b1", "pass_tight_btag_b1", "btag_score_b1",
            "E_b2", "pT_b2", "eta_b2", "phi_b2", "pass_loose_btag_b2", "pass_medium_btag_b2", "pass_tight_btag_b2", "btag_score_b2",
            "m_bb", "pT_bb",
            # light jets (ordered by pT again)
            "n_light_jets", "E_light_jets", "pT_light_jets", "eta_light_jets", "phi_light_jets",
            "pass_loose_btag_light_jets", "pass_medium_btag_light_jets", "pass_tight_btag_light_jets",
            "btag_score_light_jets",
            # first five light jets
            "E_light1", "pT_light1", "eta_light1", "phi_light1", "pass_loose_btag_light1", "pass_medium_btag_light1", "pass_tight_btag_light1", "btag_score_light1",
            "E_light2", "pT_light2", "eta_light2", "phi_light2", "pass_loose_btag_light2", "pass_medium_btag_light2", "pass_tight_btag_light2", "btag_score_light2",
            "E_light3", "pT_light3", "eta_light3", "phi_light3", "pass_loose_btag_light3", "pass_medium_btag_light3", "pass_tight_btag_light3", "btag_score_light3",
            "E_light4", "pT_light4", "eta_light4", "phi_light4", "pass_loose_btag_light4", "pass_medium_btag_light4", "pass_tight_btag_light4", "btag_score_light4",
            "E_light5", "pT_light5", "eta_light5", "phi_light5", "pass_loose_btag_light5", "pass_medium_btag_light5", "pass_tight_btag_light5", "btag_score_light5",
            # Other jet variables
            "HT", "topness",
            # three jets from the topness calculations
            "E_top_had_jet1", "pT_top_had_jet1", "eta_top_had_jet1", "phi_top_had_jet1", "pass_loose_btag_top_had_jet1", "pass_medium_btag_top_had_jet1", "pass_tight_btag_top_had_jet1", "btag_score_top_had_jet1",
            "E_top_had_jet2", "pT_top_had_jet2", "eta_top_had_jet2", "phi_top_had_jet2", "pass_loose_btag_top_had_jet2", "pass_medium_btag_top_had_jet2", "pass_tight_btag_top_had_jet2", "btag_score_top_had_jet2",
            "E_top_had_jet3", "pT_top_had_jet3", "eta_top_had_jet3", "phi_top_had_jet3", "pass_loose_btag_top_had_jet3", "pass_medium_btag_top_had_jet3", "pass_tight_btag_top_had_jet3", "btag_score_top_had_jet3",
            # W and top mass from the hadronic top decay
            "m_w_had", "pT_w_had", "eta_w_had", "phi_w_had", "E_w_had",
            ## "m_top_had", "pT_top_had", "eta_top_had", "phi_top_had",
            # b-jet and lepton invariant masses
            "m_b1l3", "m_b1l4", "m_b2l3", "m_b2l4",
            "m_b1l", "m_b2l",
            ## # delta R between b-jets and leptons
            ## "DR_b1_l1", "DR_b1_l2", "DR_b1_l3", "DR_b1_l4",
            ## "DR_b2_l1", "DR_b2_l2", "DR_b2_l3", "DR_b2_l4",
            # Missing transverse energy
            'MET', 'MET_x', 'MET_y', 'MET_phi'
        ]

        truth_higgs_list = [
            # truth Higgs
            'n_higgs', 'E_higgs', 'pT_higgs', 'eta_higgs', 'phi_higgs', 'rapidity_higgs',
            "higgs_decay_type", "n_higgs_children", 
            "higgs_child_pdgId", "higgs_child1_pdgId", "higgs_child2_pdgId"
        ] 

        truth_z_list = [
            # truth Z
            'n_Z', 'E_Z', 'pT_Z', 'eta_Z', 'phi_Z', 'rapidity_Z',
            "Z_decay_type", "n_Z_children", 
            "Z_child_pdgId", "Z_child1_pdgId", "Z_child2_pdgId"
        ]

        # combine all branches
        if self.ana_args.ttH:
            branch_list = plain["ttH"] 
            if self.ana_args.detailed:
                branch_list += list(set(photon_list + jet_list + truth_higgs_list + lepton_list + truth_HtoYY_list))
        elif self.ana_args.ttZ:
            branch_list = plain["ttZ"]
            if self.ana_args.detailed:
                branch_list += list(set(photon_list + jet_list + truth_z_list + lepton_list)) #+ truth_ZtoEE_list
        else:
            branch_list = list(set(plain["ttH"] + plain["ttZ"]))
            if self.ana_args.detailed:
                branch_list += list(set(photon_list + jet_list + truth_higgs_list + truth_z_list + lepton_list + truth_HtoYY_list)) #+ truth_ZtoEE_list

        branch_list = list(set(branch_list))
        
        return branch_list