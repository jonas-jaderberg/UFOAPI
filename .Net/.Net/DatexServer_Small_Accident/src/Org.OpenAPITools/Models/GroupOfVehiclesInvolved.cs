/*
 * DATEX II Snapshot Pull API
 *
 * This is DATEX II Snapshot PULL API returning PayloadPublication.
 *
 * The version of the OpenAPI document: 1.0.2
 * Contact: you@your-company.com
 * Generated by: https://openapi-generator.tech
 */

using System;
using System.Linq;
using System.Text;
using System.Collections.Generic;
using System.ComponentModel;
using System.ComponentModel.DataAnnotations;
using System.Runtime.Serialization;
using Newtonsoft.Json;
using Org.OpenAPITools.Converters;

namespace Org.OpenAPITools.Models
{ 
    /// <summary>
    /// 
    /// </summary>
    [DataContract]
    public partial class GroupOfVehiclesInvolved : IEquatable<GroupOfVehiclesInvolved>
    {
        /// <summary>
        /// Gets or Sets NumberOfVehicles
        /// </summary>
        [DataMember(Name="numberOfVehicles", EmitDefaultValue=true)]
        public int NumberOfVehicles { get; set; }

        /// <summary>
        /// Gets or Sets VehicleStatus
        /// </summary>
        [DataMember(Name="vehicleStatus", EmitDefaultValue=false)]
        public VehicleStatusEnumG VehicleStatus { get; set; }

        /// <summary>
        /// Gets or Sets VehicleCharacteristics
        /// </summary>
        [DataMember(Name="vehicleCharacteristics", EmitDefaultValue=false)]
        public VehicleCharacteristics VehicleCharacteristics { get; set; }

        /// <summary>
        /// Gets or Sets GroupOfVehiclesInvolvedExtensionG
        /// </summary>
        [DataMember(Name="groupOfVehiclesInvolvedExtensionG", EmitDefaultValue=false)]
        public Dictionary<string, Object> GroupOfVehiclesInvolvedExtensionG { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            var sb = new StringBuilder();
            sb.Append("class GroupOfVehiclesInvolved {\n");
            sb.Append("  NumberOfVehicles: ").Append(NumberOfVehicles).Append("\n");
            sb.Append("  VehicleStatus: ").Append(VehicleStatus).Append("\n");
            sb.Append("  VehicleCharacteristics: ").Append(VehicleCharacteristics).Append("\n");
            sb.Append("  GroupOfVehiclesInvolvedExtensionG: ").Append(GroupOfVehiclesInvolvedExtensionG).Append("\n");
            sb.Append("}\n");
            return sb.ToString();
        }

        /// <summary>
        /// Returns the JSON string presentation of the object
        /// </summary>
        /// <returns>JSON string presentation of the object</returns>
        public string ToJson()
        {
            return JsonConvert.SerializeObject(this, Formatting.Indented);
        }

        /// <summary>
        /// Returns true if objects are equal
        /// </summary>
        /// <param name="obj">Object to be compared</param>
        /// <returns>Boolean</returns>
        public override bool Equals(object obj)
        {
            if (obj is null) return false;
            if (ReferenceEquals(this, obj)) return true;
            return obj.GetType() == GetType() && Equals((GroupOfVehiclesInvolved)obj);
        }

        /// <summary>
        /// Returns true if GroupOfVehiclesInvolved instances are equal
        /// </summary>
        /// <param name="other">Instance of GroupOfVehiclesInvolved to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(GroupOfVehiclesInvolved other)
        {
            if (other is null) return false;
            if (ReferenceEquals(this, other)) return true;

            return 
                (
                    NumberOfVehicles == other.NumberOfVehicles ||
                    
                    NumberOfVehicles.Equals(other.NumberOfVehicles)
                ) && 
                (
                    VehicleStatus == other.VehicleStatus ||
                    VehicleStatus != null &&
                    VehicleStatus.Equals(other.VehicleStatus)
                ) && 
                (
                    VehicleCharacteristics == other.VehicleCharacteristics ||
                    VehicleCharacteristics != null &&
                    VehicleCharacteristics.Equals(other.VehicleCharacteristics)
                ) && 
                (
                    GroupOfVehiclesInvolvedExtensionG == other.GroupOfVehiclesInvolvedExtensionG ||
                    GroupOfVehiclesInvolvedExtensionG != null &&
                    other.GroupOfVehiclesInvolvedExtensionG != null &&
                    GroupOfVehiclesInvolvedExtensionG.SequenceEqual(other.GroupOfVehiclesInvolvedExtensionG)
                );
        }

        /// <summary>
        /// Gets the hash code
        /// </summary>
        /// <returns>Hash code</returns>
        public override int GetHashCode()
        {
            unchecked // Overflow is fine, just wrap
            {
                var hashCode = 41;
                // Suitable nullity checks etc, of course :)
                    
                    hashCode = hashCode * 59 + NumberOfVehicles.GetHashCode();
                    if (VehicleStatus != null)
                    hashCode = hashCode * 59 + VehicleStatus.GetHashCode();
                    if (VehicleCharacteristics != null)
                    hashCode = hashCode * 59 + VehicleCharacteristics.GetHashCode();
                    if (GroupOfVehiclesInvolvedExtensionG != null)
                    hashCode = hashCode * 59 + GroupOfVehiclesInvolvedExtensionG.GetHashCode();
                return hashCode;
            }
        }

        #region Operators
        #pragma warning disable 1591

        public static bool operator ==(GroupOfVehiclesInvolved left, GroupOfVehiclesInvolved right)
        {
            return Equals(left, right);
        }

        public static bool operator !=(GroupOfVehiclesInvolved left, GroupOfVehiclesInvolved right)
        {
            return !Equals(left, right);
        }

        #pragma warning restore 1591
        #endregion Operators
    }
}
